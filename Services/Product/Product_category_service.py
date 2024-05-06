import uuid
from Contracts.abc_generic_repository import AbcGenericRepository
from Helpers.uuid_helper import Uuid_helper
from Models.Product.product_category import Product_category
from Schemas.Product.Product_category_schema import Product_category_schema
from Schemas.Product.Product_schema import Product_schema


class Product_category_service():
    
    def __init__(
        self,
        repository: AbcGenericRepository[Product_category]
    ):
        self.repository = repository

    def get_all(self)-> list[Product_category]:
        return self.repository.read_by_options()


    def get_by_id(self, id: uuid.UUID) -> Product_category:
        Uuid_helper.check_valid_uuid(id)
        
        return self.repository.read_by_id(id)


    def create(self, data: Product_category_schema) -> Product_category:
        entity = Product_category(
            name = data.name
        )

        return self.repository.add(entity)


    def update(self, data: Product_category_schema) -> Product_category:
        Uuid_helper.check_valid_uuid(data.id)
        
        entity = Product_category(
            id=data.id,
            name = data.name,
        )

        return self.repository.update(entity)


    def delete(self, id: uuid.UUID):
        Uuid_helper.check_valid_uuid(id)
        
        return self.repository.delete_by_id(id)