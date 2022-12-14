# Base64 Converter

`base64-converter` is a CLI tool to quickly Base64 encode and decode strings.

## Installation

```bash
pip install --user base64-converter
```

## Usage

```bash
Usage: base64-converter [OPTIONS] COMMAND [ARGS]...

Base64 Converter

Options:
    --install-completion          Install completion for the current shell.
    --show-completion             Show completion for the current shell, to copy it or customize the installation.
    --help                        Show this message and exit.

Commands:
    d                             Base64 decode
    e                             Base64 encode
```

## Examples

### Base64 Encode

```bash
$ base64-converter e test

Output: dGVzdA==
```

### Base64 Decode

```bash
$ base64-converter e dGVzdA==

Output: test
```

## Tips & Tricks

I recommend shorthanding the CLI tool command. Be the lazy programmer.

```bash
# Linux/MacOS
$ alias b=base64-converter

# Windows
$ add alias base64-converter b

# Run Base64 Encode
$ b e test

Output: dGVzdA==

# Run Base64 Decode
$ b d dGVzdA==

Output: test
```

## Contributing

To make a contribution, fork the repo, make your changes and then submit a pull request. Please try to adhere to the existing style. If you've discovered a bug or have a feature request, create an issue.

Pending Features:

- Add code coverage GitHub badge for repository
- Support iterations to allow multiple encoding/decoding in a single line.

### Getting Started

[Install Poetry](https://python-poetry.org/docs/)

CD into the root directory and run:

```bash
# 1. It creates a virtual environment for your project
$ poetry add typer[all]

# 2. Activate that new virtual environment
$ poetry shell

# 3. Install the package
$ poetry install

# 4. Test the CLI program
$ base64-converter --help
```

## How it Works

Base64 Converter is written in Python and built on Typer. Typer is a library for building CLI applications.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
