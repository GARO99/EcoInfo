import uuid
from Contracts.abc_generic_repository import AbcGenericRepository
from Helpers.uuid_helper import Uuid_helper
from Models.Suggestion.suggestion import Suggestion
from Schemas.Suggestion.Suggestion_schema import Suggestion_schema


class Suggestion_service():

    def __init__(
        self,
        repository: AbcGenericRepository[Suggestion]
    ):
        self.repository = repository


    def get_all(self)-> list[Suggestion]:
        return self.repository.read_by_options()


    def get_by_id(self, id: uuid.UUID) -> Suggestion:
        Uuid_helper.check_valid_uuid(id)
        
        return self.repository.read_by_id(id)


    def create(self, data: Suggestion_schema) -> Suggestion:
        entity = Suggestion(
            email=data.email,
            suggest_text=data.suggest_text
        )

        return self.repository.add(entity)