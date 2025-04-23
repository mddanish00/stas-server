# stas-server

stas-server is an alternative standalone translation server for Sugoi Translator.

stas-server name is an abbreviation of Sugoi Translator Alternative Standalone Server.

Not affiliated with Sugoi Translator.

The project is in active development.

## Todo List to v1.0.0 Release

- [x] Async server (bottle.py with tornado)
- [x] Multiline support
- [x] Newlines support
- [x] Batch support
- [x] Only translate Japanese
- [x] `Access-Control-Allow-Private-Network` header
- [ ] XUAT Placeholder support
- [X] CUDA support (Tested)
- [ ] Detailed documentation
- [X] Cache support when running (Reset on Server Shutdown)
- [X] V8 and above models directory support

## User Guide

### Requirements

- Sugoi Japanese Toolkit from [MingShiba](https://www.patreon.com/mingshiba). Need to apply CudaInstallForToolKit from Sugoi Translator Discord if using version lower than V7 and below. Starting from V8, ct2Model available by default. Make sure to take note of the path to models folder.

> For V8 and above, the usual path is `[EXTRACTEDFOLDER]/Code/backendServer/Program-Backend/Sugoi-Japanese-Translator/offlineTranslation/models`.  
> For V7 and below using CudaInstallForToolKit (you need to run this first), the usual path is `[EXTRACTEDFOLDER]/Code/backendServer/Program-Backend/Sugoi-Japanese-Translator/offlineTranslation/ct2`. Inside `ct2` folder, `ct2_models` need to be renamed to `ct2Model`.

- Make sure to use Python 3.9 and above. Python 3.12 is recommended. Python 3.13 and above still not supported.

### Installation

This project is not intended as a library, so installation through `uv` and `pipx` is recommended.

In the future, the package will be published to [pypi](https://pypi.org/) for easier installation. No guarantee through.

For now, use my Python Package Index as shown as below to install this package.

You can also directly download the wheel in the [Releases](https://github.com/mddanish00/stas-server/releases) and install the package.

#### Install using uv

```commandline
uv tool install stas-server --index https://mddanish00.github.io/python-index/simple
```

#### Install using pipx

```commandline
pipx install stas-server --index-url https://mddanish00.github.io/python-index/simple
```

### Upgrade Server (outdated; not tested with python-index yet)

#### Upgrade using uv

Same as installation.

```commandline
uv tool install ./stas_server-x.x.x-py3-none-any.whl
```

#### Upgrade using pipx

Because this package is not installed from [pypi](https://pypi.org/), to upgrade this package, your need to force pipx to install the new version.

```commandline
pipx install --force ./stas_server-x.x.x-py3-none-any.whl
```

### Running Server

```cmd
Usage: stas-server [OPTIONS] [PORT]

  Run stas-server, an alternative standalone translation server for Sugoi
  Translator.

Options:
  -v, --version           Show the version and exit.
  --cuda                  Enable CUDA.
  --no-cache              Disable cache.
  --models_dir DIRECTORY  Path to models folder.  [required]
  -h, --help              Show this message and exit.
```

#### Options

|Name|Default|Description|
|----|-------|-----------|
|port|`14366`|Port of the server.|
|cuda|`false`|Enable CUDA support.|
|models_dir|`./models`|Path to models directory. By default, the program will use the folder named `models` in the current working directory.|

## Development

This project is developed using the latest Python and managed by uv.

To start developing for this project, make sure to install uv. It will automatically download uv-managed Python if your system Python not 3.12. It will not clash with your system Python because it is only used for this project.

Refer to [uv official docs](https://docs.astral.sh/uv/getting-started/installation/) for the installation instructions.

You need to make sure install ICU if in Linux yourself. For Windows, you need to use my python index to install PyICU.

Initialize the virtual environment and install dependencies.

```commandline
uv sync
```

Launch and test the server.

```commandline
uv run stas-server
```

Build the project wheel.

```commandline
uv build --wheel
```

## License

This project is licensed under the [MIT license](./LICENSE).

## Acknowledgement

- Thanks to [MingShiba](https://www.patreon.com/mingshiba) for creating the Sugoi Japanese Toolkit and making high-quality (still machine translation) available to enjoy many untranslated Japanese works.
- Thanks to Tenerezza and bimbmsm on [Sugoi Toolkit Discord](https://discord.gg/XFbWSjMHJh) for CudaInstallForToolKit script for adding CT2 support. Some of the code is based on the included CT2 multiline server script.
- Thanks to [Vin-meido](https://github.com/Vin-meido) for [Sugoi Translator XUAT](https://github.com/Vin-meido/XUnity-AutoTranslator-SugoiOfflineTranslatorEndpoint) support. Some of the code is based on the included server.py.
