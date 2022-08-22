import typer
import base64


app = typer.Typer()


@app.callback()
def callback():
    """
    Base64 Converter
    """


@app.command("e")
def encode(data: str):
    """
    Base64 encode
    """
    typer.echo(f"Data: {data}")

    data_string_bytes = data.encode("ascii")

    base64_bytes = base64.b64encode(data_string_bytes)
    base64_string = base64_bytes.decode("ascii")

    typer.echo(f"Encoded data: {base64_string}")


@app.command("d")
def decode(data: str):
    """
    Base64 decode
    """
    typer.echo(f"Data: {data}")
