from typing import Annotated
import uuid
from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from Continair.container import Container
from Models.Company.company_type import Company_Type
from Models.User.user import User
from Schemas.Company.Company_type_schema import Company_Type_Schema
from Services.Company.Company_type_service import Company_type_service


company_type_router = APIRouter(
    prefix="/companytype",
    tags=["Company Type"],
)

container = Container()
auth_service = container.authentication_service()

@company_type_router.get("/", response_model=list[Company_Type])
@inject
async def get_all(
    service: Company_type_service= Depends(Provide[Container.company_type_service])
):
    return service.get_all()


@company_type_router.get("/{id}", response_model=Company_Type)
@inject
async def get_by_id(
    id: uuid.UUID,
    service: Company_type_service= Depends(Provide[Container.company_type_service])
):
    return service.get_by_id(id)


@company_type_router.post("/", response_model=Company_Type)
@inject
async def create(
    data: Company_Type_Schema,
    user: Annotated[User, Depends(auth_service.check_session)],
    service: Company_type_service= Depends(Provide[Container.company_type_service])
):
    return service.create(data)


@company_type_router.patch("/", response_model=Company_Type)
@inject
async def update(
    data: Company_Type_Schema,
    user: Annotated[User, Depends(auth_service.check_session)],
    service: Company_type_service= Depends(Provide[Container.company_type_service])
):
    return service.update(data)


@company_type_router.delete("/{id}", status_code=204)
@inject
async def delete(
    id: uuid.UUID,
    user: Annotated[User, Depends(auth_service.check_session)],
    service: Company_type_service= Depends(Provide[Container.company_type_service])
):
    return service.delete(id)