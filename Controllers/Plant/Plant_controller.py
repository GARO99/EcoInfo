from fastapi import APIRouter

from Continair.container import Container


plant_router = APIRouter(
    prefix="/plant",
    tags=["Plant"],
)

container = Container()
auth_service = container.authentication_service()


