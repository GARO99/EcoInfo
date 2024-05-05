from fastapi import APIRouter
from Controllers.Auth.auth_controller import auth_router

routers = APIRouter()
router_list = [
    auth_router
]


for router in router_list:
    routers.include_router(router)