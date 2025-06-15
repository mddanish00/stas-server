# Using The Global Object Pattern described on
# https://python-patterns.guide/python/module-globals/.
from pathlib import Path

port = 14366
cuda = False
cache = False
models_dir = Path("./models")


# Only loaded on startup
def loads(
    enable_cuda: bool, models_dir_path: str, server_port: int, disable_cache: bool
):
    """Load config at startup

    Args:
        enable_cuda (bool): Enable CUDA support
        models_dir_path (str): Path to models folder
        server_port (int): Port to run server on
        disable_cache (bool): Disable cache
    """
    global cuda, models_dir, port, cache
    enable_cuda = enable_cuda
    models_dir = models_dir_path
    port = server_port
    cache = not disable_cache
