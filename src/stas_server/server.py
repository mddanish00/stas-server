import sys
import logging
from typing import Awaitable, Callable

from aiohttp import web
from aiocache import SimpleMemoryCache

import stas_server.config as config
from stas_server.util import (
    process_raw_string,
    split_list_by_async_condition,
    split_list_by_condition,
    recombine_split_list,
)

log_server = logging.getLogger("Server")
log_translation = logging.getLogger("Translation")
translation_cache = SimpleMemoryCache()


async def check_if_cache_exists(text: str) -> bool:
    return await translation_cache.exists(hash(text)) if config.cache else False


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
                
                key = hash(content)
                result = None
                if config.cache:
                    result = await translation_cache.get(key)

                if result is not None:
                    log_translation.info("Text is in cache.")
                else:
                    result = translate_func(content)
                    if config.cache:
                        await translation_cache.set(key, result)

                log_translation.info(f"Result: {result}")
                return web.json_response(result)
            else:
                log_translation.info("Text is not Japanese.")
                return web.json_response(content)

        elif message == "translate batch":
            content = data.get("batch")
            log_server.info("Receive content batch from server")

            if len(content) == 0:
                log_translation.info("No text in the batch.")
                return web.json_response(content)

            sp, le, ix = split_list_by_condition(content, check_func)
            sp = [process_raw_string(s) for s in sp]

            if len(sp) == 0:
                log_translation.info("All text in the batch are not Japanese.")
                return web.json_response(content)
            else:
                log_translation.info("Japanese text found in the batch.")
                (
                    cached_list,
                    rest_list,
                    index_cached_list,
                ) = await split_list_by_async_condition(sp, check_if_cache_exists)

                if len(cached_list) > 0:
                    log_translation.info("Text in batch found in cache.")

                # Fetch translations from cache
                cached_results = []
                if config.cache and len(cached_list) > 0:
                    cached_results = await translation_cache.multi_get(
                        [hash(t) for t in cached_list]
                    )

                # Translate new texts
                new_results = []
                if len(rest_list) > 0:
                    new_results = translate_batch_func(rest_list)
                    if config.cache:
                        assert len(rest_list) == len(new_results)
                        await translation_cache.multi_set(
                            zip([hash(r) for r in rest_list], new_results)
                        )

                result = recombine_split_list(
                    cached_results, new_results, index_cached_list
                )
                final_result = recombine_split_list(result, le, ix)
                return web.json_response(final_result)

        elif message == "close server":
            log_server.info("Recieved close server message. Exiting...")
            translation_cache.close()
            sys.exit(0)

        else:
            log_server.error(f"Unknown message: {message}")

        return web.json_response({"error": f"Unknown message: {message}"}, status=400)

    app = web.Application(middlewares=[cors_middleware])
    app.add_routes(
        [
            web.post("/", translate_text),
            web.options("/", lambda req: web.Response()),
        ]
    )
    log_server.info(f"Listening on http://localhost:{config.port}")
    web.run_app(
        app, host="0.0.0.0", port=config.port, access_log=log_server, print=None
    )
