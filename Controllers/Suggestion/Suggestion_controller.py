from typing import Annotated
import uuid
from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from Continair.container import Container
from Models.Suggestion.suggestion import Suggestion
from Models.User.user import User
from Schemas.Suggestion.Suggestion_schema import Suggestion_schema
from Services.Suggestion.Suggestion_service import Suggestion_service


suggestion_router = APIRouter(
    prefix="/suggestion",
    tags=["Suggestion"],
)

container = Container()
auth_service = container.authentication_service()


@suggestion_router.get("/", response_model=list[Suggestion])
@inject
async def get_all(
    user: Annotated[User, Depends(auth_service.check_session)],
    service: Suggestion_service = Depends(Provide[Container.suggestion_service])
):
    return service.get_all()


@suggestion_router.get("/{id}", response_model=Suggestion)
@inject
async def get_by_id(
    id: uuid.UUID,
    user: Annotated[User, Depends(auth_service.check_session)],
    service: Suggestion_service = Depends(Provide[Container.suggestion_service])
):
    return service.get_by_id(id)


@suggestion_router.post("/", response_model=Suggestion)
@inject
async def create(
    data: Suggestion_schema,
    service: Suggestion_service = Depends(Provide[Container.suggestion_service])
):
    return service.create(data)