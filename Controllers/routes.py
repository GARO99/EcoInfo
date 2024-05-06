from fastapi import APIRouter
from Controllers.Auth.auth_controller import auth_router
from Controllers.Company.Company_controller import company_router
from Controllers.Company.Company_type_controller import company_type_router
from Controllers.Product.Product_category_controller import product_category_router
from Controllers.Product.Product_controller import product_router
from Controllers.Store.Store_controller import store_router
from Controllers.Suggestion.Suggestion_controller import suggestion_router

routers = APIRouter()
router_list = [
    auth_router,
    company_router,
    company_type_router,
    product_category_router,
    product_router,
    store_router,
    suggestion_router
]


for router in router_list:
    routers.include_router(router)