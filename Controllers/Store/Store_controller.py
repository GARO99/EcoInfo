from typing import Annotated
import uuid
from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from Continair.container import Container
from Models.Store.store import Store
from Models.User.user import User
from Schemas.Store.Store_schema import Store_schema
from Services.Store.Store_service import Store_service


store_router = APIRouter(
    prefix="/store",
    tags=["Store"],
)

container = Container()
auth_service = container.authentication_service()


@store_router.get("/", response_model=list[Store])
@inject
async def get_all(
    service: Store_service = Depends(Provide[Container.store_service])
):
    return service.get_all()


@store_router.get("/{id}", response_model=Store)
@inject
async def get_by_id(
    id: uuid.UUID,
    service: Store_service = Depends(Provide[Container.store_service])
):
    return service.get_by_id(id)


@store_router.post("/", response_model=Store)
@inject
async def create(
    data: Store_schema,
    user: Annotated[User, Depends(auth_service.check_session)],
    service: Store_service = Depends(Provide[Container.store_service])
):
    return service.create(data)


@store_router.patch("/", response_model=Store)
@inject
async def update(
    data: Store_schema,
    user: Annotated[User, Depends(auth_service.check_session)],
    service: Store_service = Depends(Provide[Container.store_service])
):
    return service.update(data)


@store_router.delete("/{id}", status_code=204)
@inject
async def delete(
    id: uuid.UUID,
    user: Annotated[User, Depends(auth_service.check_session)],
    service: Store_service = Depends(Provide[Container.store_service])
):
    return service.delete(id)