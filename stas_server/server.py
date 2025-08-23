import sys
import logging
from typing import Awaitable, Callable

from aiohttp import web

import stas_server.config as config
from stas_server.util import (
    process_raw_string,
    split_list_by_condition,
    recombine_split_list,
)

log_server = logging.getLogger("Server")
log_translation = logging.getLogger("Translation")


def run_server(
    translate_func: Callable[[str], str],
    translate_batch_func: Callable[[list[str]], list[str]],
    check_func: Callable[[str], bool],
):
    @web.middleware
    async def cors_middleware(
        request: web.Request,
        handler: Callable[[web.Request], Awaitable[web.StreamResponse]],
    ):
        """
        You need to add some headers to each request.
        Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
        PNA (https://developer.chrome.com/blog/private-network-access-preflight)
        """
        response = await handler(request)
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add(
            "Access-Control-Allow-Methods", "PUT, GET, POST, DELETE, OPTIONS"
        )
        response.headers.add(
            "Access-Control-Allow-Headers",
            "Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token",
        )
        response.headers.add("Access-Control-Allow-Private-Network", "true")
        return response

    async def translate_text(request: web.Request):
        data = await request.json()
        message = data.get("message")

        if message == "translate sentences":
            content = data.get("content")
            log_server.info("Receive content from server")

            content = process_raw_string(content)
            if check_func(content):
                log_translation.info("Text is Japanese.")
                result = translate_func(content)
                return web.json_response(result)
            else:
                log_translation.info("Text is not Japanese.")
                return web.json_response(content)

        if message == "translate batch":
            content = data.get("batch")
            log_server.info("Receive content batch from server")

            if len(content) == 0:
                log_translation.info("No text in the batch.")
                return web.json_response(content)

            sp, le, ix = split_list_by_condition(content, check_func)
            sp = list(map(process_raw_string, sp))
            if len(sp) == 0:
                log_translation.info("All text in the batch are not Japanese.")
                return web.json_response(content)
            else:
                log_translation.info("Japanese text found in the batch.")
                result = translate_batch_func(sp)
                final_result = recombine_split_list(result, le, ix)
                return web.json_response(final_result)

        if message == "close server":
            app.shutdown()
            sys.exit(0)

    app = web.Application(middlewares=[cors_middleware])
    app.add_routes(
        [
            web.post("/", translate_text),
            web.options("/", lambda req: web.Response()),
        ]
    )
    log_server.info(f"Listening on http://localhost:{config.port}")
    web.run_app(app, port=config.port, access_log=log_server, print=None)
