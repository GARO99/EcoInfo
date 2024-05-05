import uuid
from Contracts.abc_generic_repository import AbcGenericRepository
from Helpers.uuid_helper import Uuid_helper
from Models.Company.company_type import Company_Type
from Schemas.Company.Company_type_schema import Company_Type_Schema


class Company_type_service():
    
    def __init__(
        self,
        repository: AbcGenericRepository[Company_Type]
    ):
        self.repository = repository


    def get_all(self)-> list[Company_Type]:
        return self.repository.read_by_options()


    def get_by_id(self, id: uuid.UUID) -> Company_Type:
        Uuid_helper.check_valid_uuid(id)
        
        return self.repository.read_by_id(id)


    def create(self, data: Company_Type_Schema) -> Company_Type:
        entity = Company_Type(
            name = data.name
        )

        return self.repository.add(entity)


    def update(self, data: Company_Type_Schema) -> Company_Type:
        Uuid_helper.check_valid_uuid(data.id)
        
        entity = Company_Type(
            id=data.id,
            name = data.name
        )

        return self.repository.update(entity)


    def delete(self, id: uuid.UUID):
        Uuid_helper.check_valid_uuid(id)
        
        return self.repository.delete_by_id(id)