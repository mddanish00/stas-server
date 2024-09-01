import json
from pathlib import Path

import click

DEFAULT_CONFIG = json.dumps({"port": 14366, "ct2_dir": "null", "cuda": False})
config_dir_path = Path(click.get_app_dir("stas-server"))


def initialize_config():
    config_dir_path.mkdir(exist_ok=True)
    new_config_path = config_dir_path / Path("config.json")
    new_config_path.write_text(DEFAULT_CONFIG)


def is_config_exist():
    config_path = config_dir_path / Path("config.json")
    return config_path.exists()


def load_config():
    if is_config_exist() is True:
        config_path = config_dir_path / Path("config.json")
        return generate_default_map_config(json.loads(config_path.read_text()))
    else:
        initialize_config()
        return generate_default_map_config(json.loads(DEFAULT_CONFIG))


def save_config(cuda, ct2_dir, port):
    config_path = config_dir_path / Path("config.json")
    config_path.write_text(json.dumps({"port": port, "ct2_dir": ct2_dir, "cuda": cuda}))


def generate_default_map_config(config: dict):
    return config
