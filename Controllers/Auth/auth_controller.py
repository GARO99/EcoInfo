from typing import Annotated
from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject
from fastapi.security import OAuth2PasswordRequestForm

from Config.project_config import Project_config
from Continair.container import Container
from Models.User.user import User
from Schemas.Auth.sign_in_schema import Sign_in_schema
from Schemas.Auth.token_schema import token_schema
from Schemas.User.user_info_schema import User_info_schema
from Schemas.User.user_schema import User_schema
from Services.Auth.authentication_service import Authentication_service


auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

container = Container()
auth_service = container.authentication_service()


@auth_router.post("/signIn", response_model = token_schema)
@inject
async def sign_in(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    service: Authentication_service = Depends(Provide[Container.authentication_service])
):
    sign_in_data = Sign_in_schema(
        email = form_data.username,
        password = form_data.password
    )
    
    return token_schema(access_token=service.sign_in(sign_in_data))


@auth_router.post("/signUp", response_model = User_info_schema)
@inject
async def sign_up(
    user_data: User_schema,
    service: Authentication_service = Depends(Provide[Container.authentication_service])
):
    return service.sign_up(user_data)


@auth_router.post("/signOut")
@inject
async def sign_out(
    token: Annotated[str, Depends(Project_config.OAUTH2_SCHEME())],
    service: Authentication_service = Depends(Provide[Container.authentication_service])
):
    return service.sign_out(token)


@auth_router.post("/checkSession", response_model = User_info_schema)
@inject
async def check_session(
    user: Annotated[User, Depends(auth_service.check_session)]
):
    return user