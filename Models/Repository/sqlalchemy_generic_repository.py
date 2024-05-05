import uuid

from Contracts.abc_generic_repository import AbcGenericRepository
from Exceptions.duplicated_error_exception import DuplicatedErrorException
from Exceptions.not_found_error_exception import NotFoundErrorException
from Models.Base.Base_model import Base_Model
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from typing import Callable, TypeVar, Generic

from Models.Context.sqlalchemy_context import SqlalchemyContext

Entity = TypeVar("Entity", bound=Base_Model)

class SqlAlchemyGenericRepository(AbcGenericRepository, Generic[Entity]):
    
    def __init__(self, db_context: SqlalchemyContext, entity: type[Entity]) -> None:
        self.db_context =  db_context
        self.entity = entity


    def read_by_options(self, 
        *criterion: Callable[[type[Entity]], bool],
        include_propiertys: str = str()
    ):
        with self.db_context.session() as session:
            query = session.query(self.entity)
            if len(include_propiertys) != 0:
                for propierty in include_propiertys.split(","):
                    query = query.options(joinedload(getattr(self.entity, propierty)))
            filtered_query = query.filter(*criterion)
            query = filtered_query
            query = query.all()
            return query


    def read_by_id(self,
        id: uuid.UUID,
        include_propiertys: str = str()
    ):
        with self.db_context.session() as session:
            query = session.query(self.entity)
            if len(include_propiertys) != 0:
                for propierty in include_propiertys.split(","):
                    query = query.options(joinedload(getattr(self.entity, propierty)))
            query = query.filter(self.entity.id == id).first()
            if not query:
                raise NotFoundErrorException(detail=f"not found id : {id}")
            return query


    def add(self, entity: type[Entity]):
        with self.db_context.session() as session:
            query = self.entity = entity
            try:
                session.add(query)
                session.commit()
                session.refresh(query)
            except IntegrityError as e:
                session.rollback()
                raise DuplicatedErrorException(detail=str(e.orig))
            return query


    def update(
        self,
        entity: Entity
    ):
        non_null_data = {
            attr: value for attr, value in vars(entity).items()
            if value is not None and attr != '_sa_instance_state' and attr != 'created_at'
        }

        with self.db_context.session() as session:
            session.query(self.entity).filter(self.entity.id == entity.id).update(non_null_data)
            session.commit()
            return self.read_by_id(entity.id)


    def delete_by_id(self, id: uuid.UUID):
        with self.db_context.session() as session:
            query = session.query(self.entity).filter(self.entity.id == id).first()
            if not query:
                raise NotFoundErrorException(detail=f"not found id : {id}")
            session.delete(query)
            session.commit()
    
    def delete_by_options(self, 
        *criterion: Callable[[type[Entity]], bool]
    ):
        with self.db_context.session() as session:
            query = session.query(self.entity)
            filtered_query = query.filter(*criterion)
            query = filtered_query
            query = query.all()
            if query:
                for item in query:
                    session.delete(item)
            session.commit()