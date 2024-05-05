import os
from pydantic_settings import BaseSettings


env_path = '../.env'

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