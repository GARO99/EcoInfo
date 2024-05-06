import os
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from pydantic_settings import BaseSettings


env_path = '../.env'

load_dotenv(dotenv_path=env_path)


class Project_config(BaseSettings):
    # database
    __DATABASE_URI_FORMAT: str = "{db_engine}://{user}:{password}@{host}:{port}/{database}"
    __DB_HOST: str = os.getenv("DB_HOST")
    __DB_USER: str = os.getenv("DB_USER")
    __DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    __DB_PORT: str = os.getenv("DB_PORT")
    __DB_ENGINE: str = os.getenv("DB_ENGINE")
    __DB_NAME: str = os.getenv("DB_NAME")


    # base
    @staticmethod
    def PROJECT_NAME() -> str:
        return "Eco Info API"


    @staticmethod
    def API_PREFIX() -> str:
        return "/api"


    # CORS
    @staticmethod
    def BACKEND_CORS_ORIGINS() -> list[str]:
        return ["*"]

    @staticmethod
    def SECRET_KEY() -> str:
        return "babcc327dfcc794927837331ef941c79d92165f075fb2653f6e41a7ce86fb2eb"


    @staticmethod
    def ALGORITHM() -> str:
        return "HS256"


    @staticmethod
    def OAUTH2_SCHEME() -> OAuth2PasswordBearer:
        return OAuth2PasswordBearer(tokenUrl="/api/auth/signIn")


    @property
    def DATABASE_URI(self) -> str:
        print(self.__DB_HOST)
        print(self.__DB_USER)
        print(self.__DB_PASSWORD)
        print(self.__DB_PORT)
        print(self.__DB_ENGINE)
        print(self.__DB_NAME)
        return self.__DATABASE_URI_FORMAT.format(
            db_engine=self.__DB_ENGINE,
            user=self.__DB_USER,
            password=self.__DB_PASSWORD,
            host=self.__DB_HOST,
            port=self.__DB_PORT,
            database=self.__DB_NAME,
        )