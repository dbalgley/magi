"""CLI smoke tests."""

from typer.testing import CliRunner

from magi.entrypoint import app


def test_doctor() -> None:
    """Report a healthy installation."""
    result = CliRunner().invoke(app, ["doctor"])

    assert result.exit_code == 0
    assert "healthy" in result.stdout
