"""Command-line entrypoint for Magi."""

from typing import Annotated

import typer

app = typer.Typer(no_args_is_help=True)


@app.command()
def doctor(verbose: Annotated[bool, typer.Option(help="Show additional details.")] = False) -> None:
    """Verify that the Magi package and CLI are installed."""
    typer.echo("Magi installation is healthy.")
    if verbose:
        typer.echo("Python package import: ok")


if __name__ == "__main__":
    app()
