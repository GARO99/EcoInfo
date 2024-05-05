from typing import Annotated
import uuid
from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from Continair.container import Container
from Models.Company.company import Company
from Models.User.user import User


company_router = APIRouter(
    prefix="/company",
    tags=["company"],
)

container = Container()
auth_service = container.authentication_service()


@company_router.get("/", response_model=list[Company])
@inject
async def get_all():
    pass


@company_router.get("/{id}", response_model=Company)
@inject
async def get_by_id(
    id: uuid.UUID
):
    pass


@company_router.post("/", response_model=Company)
@inject
async def create(
    user: Annotated[User, Depends(auth_service.check_session)]
):
    pass


@company_router.put("/", response_model=Company)
@inject
async def update(
    user: Annotated[User, Depends(auth_service.check_session)]
):
    pass


@company_router.delete("/{id}", status_code=204)
@inject
async def delete(
    id: uuid.UUID,
    user: Annotated[User, Depends(auth_service.check_session)]
):
    pass


