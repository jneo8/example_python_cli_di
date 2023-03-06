import click
from pydantic import BaseSettings

from example_python_cli_di.cli import cli
from example_python_cli_di.settings import Settings
from example_python_cli_di.container import Container


if __name__ == "__main__":
    container = Container()
    container.init_resources()

    container.settings.from_pydantic(Settings())
    container.wire(
        packages=["example_python_cli_di.cli"]
    )

    cli()
