from operator import and_
import uuid
from Contracts.abc_generic_repository import AbcGenericRepository
from Exceptions.app_exception import AppException
from Exceptions.not_found_error_exception import NotFoundErrorException
from Helpers.uuid_helper import Uuid_helper
from Models.Product.product_store import Product_store
from Models.Store.store import Store
from Schemas.Product.Product_store_schema import Product_store_schema
from Schemas.Store.Store_schema import Store_schema
from Services.Product.Product_service import Product_service


class Store_service():
    
    def __init__(
        self,
        store_repository: AbcGenericRepository[Store],
        product_store_repository: AbcGenericRepository[Product_store],
        product_service: Product_service
    ):
        self.store_repository = store_repository
        self.product_store_repository = product_store_repository
        self.product_service = product_service


    def get_all(self)-> list[Store]:
        return self.store_repository.read_by_options(include_propiertys="company")


    def get_by_id(self, id: uuid.UUID) -> Store:
        Uuid_helper.check_valid_uuid(id)
        
        return self.store_repository.read_by_id(id, "company")


    def create(self, data: Store_schema) -> Store:
        entity = Store(
            name = data.name,
            direction=data.direction,
            latitude=data.latitude,
            longitude=data.longitude,
            company_id=data.company_id
        )

        return self.store_repository.add(entity)

    def add_product(self, data: Product_store_schema):
        Uuid_helper.check_valid_uuid(data.product_id)
        Uuid_helper.check_valid_uuid(data.store_id)
        
        self.__valid_exist_product(data.product_id)
        self.__valid_exist_store(data.store_id)
        self.__valid_exist_product_in_store(
            data.store_id,
            data.product_id
        )
        
        entity = Product_store(
            price=data.price,
            product_id=data.product_id,
            store_id=data.store_id
        )
        
        return self.product_store_repository.add(entity)

    def update(self, data: Store_schema) -> Store:
        Uuid_helper.check_valid_uuid(data.id)
        
        entity = Store(
            id=data.id,
            name = data.name,
            direction=data.direction,
            latitude=data.latitude,
            longitude=data.longitude,
            company_id=data.company_id
        )

        return self.store_repository.update(entity)


    def delete(self, id: uuid.UUID):
        Uuid_helper.check_valid_uuid(id)
        
        return self.store_repository.delete_by_id(id)


    def __valid_exist_product(self, id: uuid.UUID):
        try:
            self.product_service.get_by_id(id)
        except NotFoundErrorException as e:
            raise AppException("El producto que intenta agregar a la tienda no existe")


    def __valid_exist_store(self, id: uuid.UUID):
        try:
            self.store_repository.read_by_id(id)
        except NotFoundErrorException as e:
            raise AppException("La tienda a la cual va relacionar los productos no existe")


    def __valid_exist_product_in_store(
        self,
        store_id: uuid.UUID,
        product_id: uuid.UUID
    ):
        criterion = lambda: and_(
            Product_store.store_id == store_id,
            Product_store.product_id  == product_id
        )
        prodcut_stores = self.product_store_repository.read_by_options(criterion)
        prodcut_store = prodcut_stores[0] if prodcut_stores else None
        
        if prodcut_store:
            raise AppException("El producto ya esta asigando a la tienda")