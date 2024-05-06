from typing import Annotated
import uuid
from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from Continair.container import Container
from Models.Product.product_category import Product_category
from Models.User.user import User
from Schemas.Product.Product_category_schema import Product_category_schema
from Services.Product.Product_category_service import Product_category_service


product_category_router = APIRouter(
    prefix="/productcategory",
    tags=["Product Category"],
)


container = Container()
auth_service = container.authentication_service()


@product_category_router.get("/", response_model=list[Product_category])
@inject
async def get_all(
    service: Product_category_service = Depends(Provide[Container.product_category_service])
):
    return service.get_all()


@product_category_router.get("/{id}", response_model=Product_category)
@inject
async def get_by_id(
    id: uuid.UUID,
    service: Product_category_service = Depends(Provide[Container.product_category_service])
):
    return service.get_by_id(id)


@product_category_router.post("/", response_model=Product_category)
@inject
async def create(
    data: Product_category_schema,
    user: Annotated[User, Depends(auth_service.check_session)],
    service: Product_category_service = Depends(Provide[Container.product_category_service])
):
    return service.create(data)


@product_category_router.patch("/", response_model=Product_category)
@inject
async def update(
    data: Product_category_schema,
    user: Annotated[User, Depends(auth_service.check_session)],
    service: Product_category_service = Depends(Provide[Container.product_category_service])
):
    return service.update(data)


@product_category_router.delete("/{id}", status_code=204)
@inject
async def delete(
    id: uuid.UUID,
    user: Annotated[User, Depends(auth_service.check_session)],
    service: Product_category_service = Depends(Provide[Container.product_category_service])
):
    return service.delete(id)