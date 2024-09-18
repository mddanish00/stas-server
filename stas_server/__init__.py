import logging

import click

from stas_server import translation, server

import importlib.metadata

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s", level=logging.INFO
)
log_server = logging.getLogger("Server")


@click.command(
    context_settings=dict(help_option_names=["-h", "--help"]),
    help="Run stas-server, an alternative standalone translation server for Sugoi Translator.",
)
@click.version_option(None, "-v", "--version", message="%(version)s")
@click.option("--cuda", default=False, is_flag=True, help="Enable CUDA.")
@click.option("--no-cache", default=False, is_flag=True, help="Disable cache.")
@click.option(
    "--models_dir",
    required=True,
    default="./models",
    help="Path to models folder.",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, resolve_path=True),
)
@click.argument("port", default=14366)
def cli(cuda, models_dir, port, no_cache):
    log_server.info(f"stas-server - v{importlib.metadata.version('stas-server')}")
    translation.setup_translation(cuda, models_dir)
    server.run_server(
        translation.translate,
        translation.translate_batch,
        translation.check_if_japanese_in_string,
        port,
        not no_cache,
    )
