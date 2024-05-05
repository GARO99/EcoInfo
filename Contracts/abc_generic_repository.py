import uuid
from abc import ABC, abstractmethod
from typing import Callable, Generic, TypeVar

from Models.Base.Base_model import Base_Model


Entity = TypeVar("Entity", bound=Base_Model)

class AbcGenericRepository(ABC, Generic[Entity]):

    @abstractmethod
    def read_by_options(
        self,
        *criterion: Callable[[type[Entity]], bool],
        include_propiertys: str = str()
    ):
        pass


    @abstractmethod
    def read_by_id(
        self,
        id: uuid.UUID,
        include_propiertys: str = str()
    ):
        pass


    @abstractmethod
    def add(
        self,
        entity: type[Entity]
    ):
        pass


    @abstractmethod
    def update(
        self,
        entity: type[Entity]
    ):
        pass


    @abstractmethod
    def delete_by_id(self, id: uuid.UUID):
        pass


    @abstractmethod
    def delete_by_options(
        self,
        *criterion: Callable[[type[Entity]], bool]
    ):
        pass
