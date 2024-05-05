from Continair.container import Container
from Controllers.routes import routers
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from Config.project_config import Project_config
from Middlewares.exception_handler_middleware import Exception_Handler_Middleware
from Utils.singleton import singleton


@singleton
class AppCreator:
    def __init__(self):
        # set app default
        self.app = FastAPI(
            title=Project_config.PROJECT_NAME(),
            version="0.0.1",
        )

        # set db and container
        self.container = Container()
        self.db = self.container.db()

        # set cors
        if Project_config.BACKEND_CORS_ORIGINS():
            self.app.add_middleware(
                CORSMiddleware,
                allow_origins=[str(origin) for origin in Project_config.BACKEND_CORS_ORIGINS()],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )

        #middlewares
        self.app.add_middleware(Exception_Handler_Middleware)

        # set routes
        @self.app.get("/")
        def root():
            return "service is working"

        self.app.include_router(
            routers, prefix=Project_config.API_PREFIX())


app_creator = AppCreator()
app = app_creator.app
db = app_creator.db
container = app_creator.container