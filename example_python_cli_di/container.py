from dependency_injector import containers, providers
from example_python_cli_di.logger import get_logger

class Container(containers.DeclarativeContainer):

    settings = providers.Configuration()
    logger = providers.Singleton(get_logger)
