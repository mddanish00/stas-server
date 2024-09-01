import json
import sys
import logging
from typing import Callable

from bottle import Bottle, request, response

from stas_server.fringe_list_util import (
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
    translate_func: Callable[[str], str],
    translate_batch_func: Callable[[list[str]], list[str]],
    check_func: Callable[[str], bool],
    port: int = 14366,
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
            if check_func(content):
                log_translation.info("Text is Japanese.")
                result = translate_func(content)
                return json.dumps(result)
            else:
                log_translation.info(f"Text is not Japanese.")
                return json.dumps(content)

        if message == "translate batch":
            content = data.get("batch")
            log_server_bottle.info("Receive content batch from server")

            s, l, i = split_list_by_condition(content, check_func)
            if len(s) == 0:
                log_translation.info(f"All text in the batch are not Japanese.")
                return json.dumps(content)
            else:
                log_translation.info(f"Japanese text found in the batch.")
                result = translate_batch_func(content)
                final_result = recombine_split_list(result, l, i)
                return json.dumps(final_result)

        if message == "close server":
            app.close()
            sys.exit(0)

    log_server_bottle.info(f"Listening on http://localhost:{port}")
    app.run(server="tornado", host="localhost", port=port, debug=False, quiet=True)