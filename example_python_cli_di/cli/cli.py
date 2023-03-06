import logging
import typing as t

import click
from dependency_injector.wiring import Provide, inject
from pydantic import BaseSettings
from example_python_cli_di.container import Container
from example_python_cli_di.settings import Settings


class UserObj(BaseSettings):
    settings: t.Optional[Settings] = None
    logger: t.Optional[logging.Logger] = None


    def pre_check(self):
        assert self.settings is not None
        assert self.logger is not None



@click.group()
@click.pass_context
@inject
def cli(
    ctx,
    settings: Settings = Provide[Container.settings],
    logger: logging.Logger = Provide[Container.logger],
):
    ctx.ensure_object(UserObj)
    ctx.obj.settings = settings
    ctx.obj.logger = logger
    ctx.obj.pre_check()


def cli_command(func):
    for option in reversed([
        cli.command(),
        click.pass_context,
    ]):
        func = option(func)
    return func


@cli_command
def cmd1(ctx):
    logger = ctx.obj.logger
    logger.debug("cmd1")
