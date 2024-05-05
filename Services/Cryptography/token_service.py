from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt

from Config.project_config import Project_config
from Contracts.abc_generic_repository import AbcGenericRepository
from Exceptions.unauthorized_exception import UnauthorizedException
from Models.Token.token_blacklist import Token_blacklist


class Token_service():
    
    def __init__(
        self,
        repository: AbcGenericRepository[Token_blacklist]
    ):
        self.repository = repository
    
    def create_access_jwt_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(hours=24)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, Project_config.SECRET_KEY(), algorithm=Project_config.ALGORITHM())
        return encoded_jwt


    def validate_jwt_token(self, token: str) -> str:
        try:
            payload = jwt.decode(token, Project_config.SECRET_KEY(), algorithms=[Project_config.ALGORITHM()])
            id: str = payload.get("id")
            if id is None:
                raise UnauthorizedException("Token invalido")
        
            return id
        except JWTError:
            raise UnauthorizedException("Token invalido")


    def add_blacklist(self, token: str):
        blacklist = Token_blacklist(expires_token=token)
        self.repository.add(blacklist)


    def valid_token_blacklist(self, token: str) -> bool:
        criterion = lambda: (Token_blacklist.expires_token == token)
        token_blacklists = self.repository.read_by_options(criterion)
        token_blacklist = token_blacklists[0] if token_blacklists else None
        if token_blacklist:
            return True
        else:
            return False