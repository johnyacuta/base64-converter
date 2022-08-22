from base64_converter import __version__
from typer.testing import CliRunner
from base64_converter.main import app


runner = CliRunner()


def test_version():
    assert __version__ == '0.1.0'


def test_base64_encode():
    result = runner.invoke(app, ["e", "test"])
    assert result.exit_code == 0
    assert "dGVzdA==" in result.stdout


def test_base64_decode():
    result = runner.invoke(app, ["d", "dGVzdA=="])
    assert result.exit_code == 0
    assert "test" in result.stdout
