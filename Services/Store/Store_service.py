import uuid
from Contracts.abc_generic_repository import AbcGenericRepository
from Helpers.uuid_helper import Uuid_helper
from Models.Store.store import Store
from Schemas.Store.Store_schema import Store_schema


class Store_service():
    
    def __init__(
        self,
        repository: AbcGenericRepository[Store]
    ):
        self.repository = repository


    def get_all(self)-> list[Store]:
        return self.repository.read_by_options()


    def get_by_id(self, id: uuid.UUID) -> Store:
        Uuid_helper.check_valid_uuid(id)
        
        return self.repository.read_by_id(id)


    def create(self, data: Store_schema) -> Store:
        entity = Store(
            name = data.name,
            direction=data.direction,
            latitude=data.latitude,
            longitude=data.longitude,
            company_id=data.company_id
        )

        return self.repository.add(entity)


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

        return self.repository.update(entity)


    def delete(self, id: uuid.UUID):
        Uuid_helper.check_valid_uuid(id)
        
        return self.repository.delete_by_id(id)