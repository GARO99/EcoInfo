from dependency_injector import containers, providers

from Config.project_config import Project_config
from Models.Context.sqlalchemy_context import SqlalchemyContext


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "Controllers"
        ]
    )
    
    db = providers.Singleton(
        SqlalchemyContext,
        db_url = Project_config().DATABASE_URI
    )