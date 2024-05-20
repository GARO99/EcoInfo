import uuid
from Contracts.abc_generic_repository import AbcGenericRepository
from Helpers.uuid_helper import Uuid_helper
from Models.Product.product import Product
from Schemas.Product.Product_schema import Product_schema


class Product_service():
    
    def __init__(
        self,
        repository: AbcGenericRepository[Product]
    ):
        self.repository = repository


    def get_all(self)-> list[Product]:
        return self.repository.read_by_options(include_propiertys="product_category")


    def get_by_id(self, id: uuid.UUID) -> Product:
        Uuid_helper.check_valid_uuid(id)
        
        return self.repository.read_by_id(id, "product_category")


    def create(self, data: Product_schema) -> Product:
        entity = Product(
            name = data.name,
            description=data.description,
            brand=data.brand,
            product_category_id=data.product_category_id
        )

        return self.repository.add(entity)


    def update(self, data: Product_schema) -> Product:
        Uuid_helper.check_valid_uuid(data.id)
        
        entity = Product(
            id=data.id,
            name = data.name,
            description=data.description,
            brand=data.brand,
            product_category_id=data.product_category_id
        )

        return self.repository.update(entity)


    def delete(self, id: uuid.UUID):
        Uuid_helper.check_valid_uuid(id)
        
        return self.repository.delete_by_id(id)