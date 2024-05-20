import uuid
from Contracts.abc_generic_repository import AbcGenericRepository
from Helpers.uuid_helper import Uuid_helper
from Models.Company.company import Company
from Schemas.Company.Company_schema import Company_Schema


class Company_service():

    def __init__(
        self,
        repository: AbcGenericRepository[Company]
    ):
        self.repository = repository


    def get_all(self)-> list[Company]:
        return self.repository.read_by_options(include_propiertys="company_type")


    def get_by_id(self, id: uuid.UUID) -> Company:
        Uuid_helper.check_valid_uuid(id)
        
        return self.repository.read_by_id(id, "company_type")


    def create(self, data: Company_Schema) -> Company:
        entity = Company(
            name = data.name,
            company_type_id=data.company_type_id
        )

        return self.repository.add(entity)


    def update(self, data: Company_Schema) -> Company:
        Uuid_helper.check_valid_uuid(data.id)
        
        entity = Company(
            id=data.id,
            name = data.name,
            company_type_id=data.company_type_id
        )

        return self.repository.update(entity)


    def delete(self, id: uuid.UUID):
        Uuid_helper.check_valid_uuid(id)
        
        return self.repository.delete_by_id(id)