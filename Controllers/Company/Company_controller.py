from typing import Annotated
import uuid
from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from Continair.container import Container
from Models.Company.company import Company
from Models.User.user import User
from Schemas.Company.Company_response_schema import Company_Response_Schema
from Schemas.Company.Company_schema import Company_Schema
from Services.Company.Company_service import Company_service


company_router = APIRouter(
    prefix="/company",
    tags=["Company"],
)

container = Container()
auth_service = container.authentication_service()


@company_router.get("/", response_model=list[Company_Response_Schema])
@inject
async def get_all(
    service: Company_service= Depends(Provide[Container.company_service])
):
    return service.get_all()


@company_router.get("/{id}", response_model=Company_Response_Schema)
@inject
async def get_by_id(
    id: uuid.UUID,
    service: Company_service= Depends(Provide[Container.company_service])
):
    return service.get_by_id(id)


@company_router.post("/", response_model=Company)
@inject
async def create(
    data: Company_Schema,
    user: Annotated[User, Depends(auth_service.check_session)],
    service: Company_service= Depends(Provide[Container.company_service])
):
    return service.create(data)


@company_router.patch("/", response_model=Company)
@inject
async def update(
    data: Company_Schema,
    user: Annotated[User, Depends(auth_service.check_session)],
    service: Company_service= Depends(Provide[Container.company_service])
):
    return service.update(data)


@company_router.delete("/{id}", status_code=204)
@inject
async def delete(
    id: uuid.UUID,
    user: Annotated[User, Depends(auth_service.check_session)],
    service: Company_service= Depends(Provide[Container.company_service])
):
    return service.delete(id)