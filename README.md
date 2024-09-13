# stas-server

stas-server is an alternative standalone translation server for Sugoi Translator.

stas-server name is an abbreviation of Sugoi Translator Alternative Standalone Server. 

Not affiliated with Sugoi Translator.

The project is in active development.

## Todo List

- [x] Async server (bottle.py with tornado)
- [x] Multiline support
- [x] Newlines support
- [x] Batch support
- [x] Only translate Japanese
- [x] `Access-Control-Allow-Private-Network` header
- [ ] XUAT Placeholder support
- [X] CUDA support (not tested because I don't have Nvidia GPU)
- [ ] Detailed documentation

## User Guide

### Requirements

- Sugoi Japanese Toolkit from [MingShiba](https://www.patreon.com/mingshiba) with CudaInstallForToolKit from Sugoi Translator Discord if using version lower than V7 and below. Make sure to take note of the path to ct2 folder.

- Make sure to use Python 3.9 and above. Python 3.12 is recommended.

- Node is also required. Make sure to use the latest major LTS version or higher. Only used during installation.

### Installation

This project is not intended as a library, so installation through `pipx` or `uv` is recommended.

In the future, the package will be published to [pypi](https://pypi.org/) for easier installation. No guarantee through.

Download the wheel in the [Releases](https://github.com/mddanish00/stas-server/releases) and install the package.

#### Using pipx

```commandline
pipx install ./stas_server-x.x.x-py3-none-any.whl
```

#### Using uv

```commandline
uv tool install ./stas_server-x.x.x-py3-none-any.whl
```
### Upgrade Server

#### Using pipx

Because this package is not installed from [pypi](https://pypi.org/), to upgrade this package, your need to force pipx to install the new version.

```commandline
pipx install --force ./stas_server-x.x.x-py3-none-any.whl
```

#### Using uv

Same as installation.

```commandline
uv tool install ./stas_server-x.x.x-py3-none-any.whl
```

### Running Server

```
Usage: stas-server [OPTIONS] [PORT]

  Run stas-server, an alternative standalone translation server for Sugoi
  Translator.

Options:
  -v, --version        Show the version and exit.
  --cuda               Enable CUDA.
  --ct2_dir DIRECTORY  Path to ct2 folder.  [required]
  -h, --help           Show this message and exit.
```

#### Options

|Name|Default|Description|
|----|-------|-----------|
|port|`14366`|Port of the server.|
|cuda|`false`|Enable CUDA support.|
|ct2_dir|`./ct2`|Path to ct2 models directory. By default, the program will use the folder named `ct2` in the current working directory.|

## Development

This project is developed using the latest Python and managed by Rye.

To start developing for this project, make sure to install Rye. It will automatically download Rye-managed Python. It will not clash with your system Python because it is only used for this project.

Refer to [Rye official docs](https://rye.astral.sh/guide/installation) for the installation instructions.

Node also needed during installation because this project is using, [PythonMonkey](https://github.com/Distributive-Network/PythonMonkey). The latest Node LTS is used during development.

Initialize venv and install dependencies.

```commandline
rye sync
```

Launch and test the server.

```commandline
rye run stas-server
```

Build the project wheel.

```commandline
rye build -c --wheel
```

## License

This project is licensed under the [MIT license](./LICENSE).

## Acknowledgement

- Thanks to [MingShiba](https://www.patreon.com/mingshiba) for creating the Sugoi Japanese Toolkit and making high-quality (still machine translation) available to enjoy many untranslated Japanese works.
- Thanks to Tenerezza and bimbmsm on [Sugoi Toolkit Discord](https://discord.gg/XFbWSjMHJh) for CudaInstallForToolKit script for adding CT2 support. Some of the code is based on the included CT2 multiline server script.
- Thanks to [Vin-meido](https://github.com/Vin-meido) for [Sugoi Translator XUAT](https://github.com/Vin-meido/XUnity-AutoTranslator-SugoiOfflineTranslatorEndpoint) support. Some of the code is based on the included server script.
