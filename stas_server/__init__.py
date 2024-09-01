import logging

import click

from stas_server import translation, server, config

import importlib.metadata

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s", level=logging.INFO
)
log_server = logging.getLogger("Server")

CONTEXT_SETTINGS = dict(
    help_option_names=["-h", "--help"], default_map=config.load_config()
)


@click.command(context_settings=CONTEXT_SETTINGS, help="Start this translation server.")
@click.version_option(None, "-v", "--version", message="%(version)s")
@click.option("--cuda", default=False, is_flag=True, help="Enable CUDA.")
@click.option(
    "--ct2_dir",
    required=True,
    help="Path to ct2 folder.",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, resolve_path=True),
)
@click.argument("port", default=14366)
def cli(cuda, ct2_dir, port):
    log_server.info(
        f"stas-server - v{importlib.metadata.version('stas-server')}"
    )
    translation.setup_translation(cuda, ct2_dir)
    server.run_server(
        translation.translate,
        translation.translate_batch,
        translation.check_if_japanese_in_string,
        port,
    )


@click.command(
    context_settings=CONTEXT_SETTINGS, help="Save the configuration for future uses."
)
@click.option("--cuda", default=False, is_flag=True, help="Enable CUDA.")
@click.option(
    "--ct2_dir",
    help="Path to ct2 folder.",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, resolve_path=True),
)
@click.option("--port", default=14366, help="Port of the server.")
@click.option(
    "--reset",
    default=False,
    is_flag=True,
    help="Save the default configuration. Other options will be ignored when this flag present.",
)
def config_cli(cuda, ct2_dir, port, reset):
    if reset:
        config.initialize_config()
    else:
        config.save_config(cuda, ct2_dir, port)