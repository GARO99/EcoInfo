from typing import TYPE_CHECKING, Optional
import uuid
from sqlmodel import Field, Relationship

from Models.Base.Base_model import Base_Model
from Models.Company.company_type import Company_Type

if TYPE_CHECKING:
    from Models.Store.store import Store


class Company(Base_Model, table=True):
    name: str = Field(default=None, nullable=False, max_length= 100)
    company_type_id: uuid.UUID = Field(default=None, nullable=False, foreign_key="company_type.id")

    company_type: Optional[Company_Type] = Relationship(back_populates="companys")
    stores: list["Store"] = Relationship(back_populates="company")