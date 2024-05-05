from dependency_injector import containers, providers

from Config.project_config import Project_config
from Models.Context.sqlalchemy_context import SqlalchemyContext
from Models.Repository.sqlalchemy_generic_repository import SqlAlchemyGenericRepository
from Models.Token.token_blacklist import Token_blacklist
from Models.User.user import User
from Services.Auth.authentication_service import Authentication_service
from Services.Cryptography.token_service import Token_service
from Services.User.user_service import User_service


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "Controllers.Auth.auth_controller"
        ]
    )
    
    db = providers.Singleton(
        SqlalchemyContext,
        db_url = Project_config().DATABASE_URI
    )
    
    generic_repository_user = providers.Factory(
        SqlAlchemyGenericRepository,
        db_context=db.provided,
        entity=User
    )

    user_service = providers.Factory(
        User_service,
        repository=generic_repository_user
    )


    generic_repository_token = providers.Factory(
        SqlAlchemyGenericRepository,
        db_context=db.provided,
        entity=Token_blacklist
    )

    token_service = providers.Factory(
        Token_service,
        repository=generic_repository_token
    )


    authentication_service = providers.Factory(
        Authentication_service,
        user_service=user_service,
        token_service=token_service
    )