from dependency_injector import containers, providers

from Config.project_config import Project_config
from Models.Company.company import Company
from Models.Company.company_type import Company_Type
from Models.Context.sqlalchemy_context import SqlalchemyContext
from Models.Product.product import Product
from Models.Product.product_category import Product_category
from Models.Product.product_store import Product_store
from Models.Repository.sqlalchemy_generic_repository import SqlAlchemyGenericRepository
from Models.Store.store import Store
from Models.Suggestion.suggestion import Suggestion
from Models.Token.token_blacklist import Token_blacklist
from Models.User.user import User
from Services.Auth.authentication_service import Authentication_service
from Services.Company.Company_service import Company_service
from Services.Company.Company_type_service import Company_type_service
from Services.Cryptography.token_service import Token_service
from Services.Product.Product_category_service import Product_category_service
from Services.Product.Product_service import Product_service
from Services.Store.Store_service import Store_service
from Services.Suggestion.Suggestion_service import Suggestion_service
from Services.User.user_service import User_service


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "Controllers.Auth.auth_controller",
            "Controllers.Company.Company_controller",
            "Controllers.Company.Company_type_controller",
            "Controllers.Product.Product_category_controller",
            "Controllers.Product.Product_controller",
            "Controllers.Store.Store_controller",
            "Controllers.Suggestion.Suggestion_controller"
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


    generic_repository_company_type = providers.Factory(
        SqlAlchemyGenericRepository,
        db_context=db.provided,
        entity=Company_Type
    )

    company_type_service = providers.Factory(
        Company_type_service,
        repository=generic_repository_company_type
    )


    generic_repository_company= providers.Factory(
        SqlAlchemyGenericRepository,
        db_context=db.provided,
        entity=Company
    )

    company_service = providers.Factory(
        Company_service,
        repository=generic_repository_company
    )


    generic_repository_product_category= providers.Factory(
        SqlAlchemyGenericRepository,
        db_context=db.provided,
        entity=Product_category
    )

    product_category_service = providers.Factory(
        Product_category_service,
        repository=generic_repository_product_category
    )


    generic_repository_product = providers.Factory(
        SqlAlchemyGenericRepository,
        db_context=db.provided,
        entity=Product
    )

    product_service = providers.Factory(
        Product_service,
        repository=generic_repository_product
    )


    generic_repository_store = providers.Factory(
        SqlAlchemyGenericRepository,
        db_context=db.provided,
        entity=Store
    )

    generic_repository_product_store = providers.Factory(
        SqlAlchemyGenericRepository,
        db_context=db.provided,
        entity=Product_store
    )

    store_service = providers.Factory(
        Store_service,
        store_repository=generic_repository_store,
        product_store_repository=generic_repository_product_store,
        product_service=product_service
    )


    generic_repository_suggestion = providers.Factory(
        SqlAlchemyGenericRepository,
        db_context=db.provided,
        entity=Suggestion
    )

    suggestion_service = providers.Factory(
        Suggestion_service,
        repository=generic_repository_suggestion
    )
