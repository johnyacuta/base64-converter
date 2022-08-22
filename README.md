# Base64 Converter

`base64-converter` is a CLI tool to quickly Base64 encode and decode strings.

## Installation - TBD

```bash
pip install --user <TBD>
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
