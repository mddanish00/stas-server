import json
import sys
import logging
from typing import Callable

from bottle import Bottle, request, response

from stas_server.util import (
    process_raw_string,
    split_list_by_condition,
    recombine_split_list,
)

log_server_bottle = logging.getLogger("Server")
log_translation = logging.getLogger("Translation")

app = Bottle()


def route(**kwargs):
    def decorator(callback):
        kwargs["callback"] = callback
        app.route(**kwargs)

        kwargs["method"] = "OPTIONS"
        kwargs["callback"] = lambda: {}
        app.route(**kwargs)
        return callback

    return decorator


def run_server(
    translate_func: Callable[[str, bool], str],
    translate_batch_func: Callable[[list[str], bool], list[str]],
    check_func: Callable[[str], bool],
    port: int = 14366,
    enable_cache: bool = True,
):
    @app.hook("after_request")
    def enable_cors():
        """
        You need to add some headers to each request.
        Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
        PNA (https://developer.chrome.com/blog/private-network-access-preflight)
        """
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = (
            "PUT, GET, POST, DELETE, OPTIONS"
        )
        response.headers["Access-Control-Allow-Headers"] = (
            "Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token"
        )
        response.headers["Access-Control-Allow-Private-Network"] = "true"

    @route(path="/", method="POST")
    def translate_text():
        data = request.json
        message = data.get("message")

        if message == "translate sentences":
            content = data.get("content")
            log_server_bottle.info("Receive content from server")

            content = process_raw_string(content)
            if check_func(content):
                log_translation.info("Text is Japanese.")
                result = translate_func(content, enable_cache)
                return json.dumps(result)
            else:
                log_translation.info("Text is not Japanese.")
                return json.dumps(content)

        if message == "translate batch":
            content = data.get("batch")
            log_server_bottle.info("Receive content batch from server")

            if len(content) == 0:
                log_translation.info("No text in the batch.")
                return json.dumps(content)

            sp, le, ix = split_list_by_condition(content, check_func)
            sp = list(map(process_raw_string, sp))
            if len(sp) == 0:
                log_translation.info("All text in the batch are not Japanese.")
                return json.dumps(content)
            else:
                log_translation.info("Japanese text found in the batch.")
                result = translate_batch_func(sp, enable_cache)
                final_result = recombine_split_list(result, le, ix)
                return json.dumps(final_result)

        if message == "close server":
            app.close()
            sys.exit(0)

    log_server_bottle.info(f"Listening on http://localhost:{port}")
    app.run(server="tornado", host="0.0.0.0", port=port, debug=False, quiet=True)
