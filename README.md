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

- Sugoi Japanese Toolkit from [MingShiba](https://www.patreon.com/mingshiba). If you are using a version lower than V7, you need to apply CudaInstallForToolKit from the Sugoi Translator Discord. Starting from V8, ct2Model is available by default. Make sure to note the path to the models folder.

> For V8 and above, the usual path is `[EXTRACTEDFOLDER]/Code/backendServer/Program-Backend/Sugoi-Japanese-Translator/offlineTranslation/models`.  
> For V7 and below using CudaInstallForToolKit (you need to run this first), the usual path is `[EXTRACTEDFOLDER]/Code/backendServer/Program-Backend/Sugoi-Japanese-Translator/offlineTranslation/ct2`. Inside the `ct2` folder, `ct2_models` needs to be renamed to `ct2Model`.

- Python 3.12 recommended. For Python 3.13, you **absolutely** need to use [my Python Package Index](https://mddanish00.github.io/python-index/simple). Python 3.14 and above are still not supported.

### Installation

This project is not intended as a library, so installation through `uv` is recommended.

It is recommended to use [my Python Package Index](https://mddanish00.github.io/python-index/simple) for as shown as below to install this package.

You can also directly download the wheel in the [Releases](https://github.com/mddanish00/stas-server/releases) and install the package.

#### Install using uv

```commandline
uv tool install stas-server --index https://mddanish00.github.io/python-index/simple
```

### Upgrade Server

#### Upgrade using uv

```commandline
uv tool upgrade stas-server
```

### Running Server

```cmd
usage: stas-server [OPTIONS] [PORT]

Run stas-server, an alternative standalone translation server for Sugoi Translator.

positional arguments:
  port                  Port to listen on. (default: 14366)

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --cuda                Enable CUDA. (default: False)
  --no-cache            Disable cache. (default: False)
  --models_dir MODELS_DIR
                        Path to models folder. (default: None)
```

#### Options

|Name|Default|Description|
|----|-------|-----------|
|port|`14366`|Port of the server.|
|cuda|`false`|Enable CUDA support.|
|models_dir|`./models`|Path to models directory. By default, the program will use the folder named `models` in the current working directory.|

## Development

This project is developed using the latest Python and managed by uv.

To start developing for this project, make sure to install uv. It will automatically download uv-managed Python if your system Python is not 3.13. It will not clash with your system Python because it is only used for this project.

Refer to [uv official docs](https://docs.astral.sh/uv/getting-started/installation/) for the installation instructions.

You need to make sure install ICU if in Linux yourself. For Windows, you need to use my python index to install PyICU.

Initialise the virtual environment and install dependencies.

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
