from fastapi import APIRouter
from Controllers.Auth.auth_controller import auth_router
from Controllers.Company.Company_controller import company_router
from Controllers.Company.Company_type_controller import company_type_router

routers = APIRouter()
router_list = [
    auth_router,
    company_router,
    company_type_router
]


for router in router_list:
    routers.include_router(router)