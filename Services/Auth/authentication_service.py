from typing import Annotated
import uuid

from fastapi import Depends
from Config.project_config import Project_config
from Contracts.abc_generic_repository import AbcGenericRepository
from Exceptions.app_exception import AppException
from Exceptions.unauthorized_exception import UnauthorizedException
from Helpers.validate_helper import Validate_helper
from Models.User.user import User
from Schemas.Auth.sign_in_schema import Sign_in_schema
from Schemas.User.user_schema import User_schema
from Services.Cryptography.token_service import Token_service
from Services.User.user_service import User_service


class Authentication_service():

    def __init__(
        self,
        user_service: User_service,
        token_service: Token_service
    ):
        self.user_service = user_service
        self.token_service = token_service


    def sign_in(self, sing_in_data: Sign_in_schema)-> str:
        if not Validate_helper.validate_email(sing_in_data.email):
            raise AppException("El correo electrónico no es valido.")
        
        user: User = self.user_service.get_user_by_email(sing_in_data.email)
        
        if not user:
            raise UnauthorizedException("El correo electrónico proporcionado no está asociado con ninguna cuenta registrada. Por favor, verifique su correo electrónico o regístrese para crear una cuenta nueva.")
        
        if user.password != sing_in_data.password:
            raise UnauthorizedException("La contraseña proporcionada es incorrecta. Por favor, inténtelo de nuevo.")
        
        data={"id": str(user.id)}
        
        return self.token_service.create_access_jwt_token(data)


    def sign_up(self, user_data: User_schema) -> User:
        if not Validate_helper.validate_email(user_data.email):
            raise AppException("El correo electrónico no es valido.")
        
        exit_user: User = self.user_service.get_user_by_email(user_data.email)
        
        if exit_user:
            raise AppException("El correo electrónico que ingreso ya está asociado con un cuenta.")
        
        entity = User(
            name = user_data.name,
            last_name = user_data.last_name,
            email= user_data.email,
            password = user_data.password
        )
        
        return self.user_service.create(entity)


    def sign_out(self, token: str):
        self.token_service.add_blacklist(token)


    async def check_session(self, token: Annotated[str, Depends(Project_config.OAUTH2_SCHEME())]):
        if self.token_service.valid_token_blacklist(token):
            raise UnauthorizedException("Token invalido")
        
        id = uuid.UUID(self.token_service.validate_jwt_token(token))
        user: User = self.user_service.get_user_by_id(id)
        
        if not user:
            raise UnauthorizedException("Token invalido")
        
        return user