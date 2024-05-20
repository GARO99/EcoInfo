from typing import Annotated
import uuid
from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from Continair.container import Container
from Models.Product.product import Product
from Models.User.user import User
from Schemas.Product.Product_response_schema import Product_response_schema
from Schemas.Product.Product_schema import Product_schema
from Services.Product.Product_service import Product_service


product_router = APIRouter(
    prefix="/product",
    tags=["Product"],
)


container = Container()
auth_service = container.authentication_service()


@product_router.get("/", response_model=list[Product_response_schema])
@inject
async def get_all(
    service: Product_service = Depends(Provide[Container.product_service])
):
    return service.get_all()


@product_router.get("/{id}", response_model=Product_response_schema)
@inject
async def get_by_id(
    id: uuid.UUID,
    service: Product_service = Depends(Provide[Container.product_service])
):
    return service.get_by_id(id)


@product_router.post("/", response_model=Product)
@inject
async def create(
    data: Product_schema,
    user: Annotated[User, Depends(auth_service.check_session)],
    service: Product_service = Depends(Provide[Container.product_service])
):
    return service.create(data)


@product_router.patch("/", response_model=Product)
@inject
async def update(
    data: Product_schema,
    user: Annotated[User, Depends(auth_service.check_session)],
    service: Product_service = Depends(Provide[Container.product_service])
):
    return service.update(data)


@product_router.delete("/{id}", status_code=204)
@inject
async def delete(
    id: uuid.UUID,
    user: Annotated[User, Depends(auth_service.check_session)],
    service: Product_service = Depends(Provide[Container.product_service])
):
    return service.delete(id)