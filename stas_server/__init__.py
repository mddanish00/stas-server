import logging
import argparse
from importlib.metadata import version
import os

from stas_server import config, translation, server

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s", level=logging.INFO
)
log_server = logging.getLogger("Server")
current_version = version("stas-server")


def get_arguments() -> tuple[bool, str, int, bool]:
    parser = argparse.ArgumentParser(
        description="Run stas-server, an alternative standalone translation server for Sugoi Translator.",
        usage="%(prog)s [OPTIONS] [PORT]",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=current_version,
    )
    parser.add_argument("--cuda", action="store_true", help="Enable CUDA.")
    parser.add_argument("--no-cache", action="store_true", help="Disable cache.")
    parser.add_argument(
        "--models_dir",
        required=True,
        help="Path to models folder.",
    )
    parser.add_argument(
        "port",
        type=int,
        nargs="?",
        default=14366,
        help="Port to listen on.",
    )

    args = parser.parse_args()

    models_dir = os.path.abspath(args.models_dir)
    if not os.path.isdir(models_dir):
        parser.error(f"The models directory does not exist: '{models_dir}'")

    return args.cuda, models_dir, args.port, args.no_cache


def cli():
    cuda, models_dir, port, no_cache = get_arguments()

    config.loads(cuda, models_dir, port, no_cache)
    log_server.info(f"stas-server - v{current_version}")
    translation.setup_translation()
    server.run_server(
        translation.translate,
        translation.translate_batch,
        translation.check_if_japanese_in_string,
    )
