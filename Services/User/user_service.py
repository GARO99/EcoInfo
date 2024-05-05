import uuid
from Contracts.abc_generic_repository import AbcGenericRepository
from Models.User.user import User


class User_service():
    
    def __init__(
        self,
        repository: AbcGenericRepository[User]
    ):
        self.repository = repository


    def get_user_by_email(self, email: str):
        criterion = lambda: (User.email == email)
        users = self.repository.read_by_options(criterion)
        user = users[0] if users else None
        return user


    def get_user_by_id(self, id: uuid.UUID):
        return self.repository.read_by_id(id)


    def create(self, user_data: User) -> User:
        return self.repository.add(user_data)