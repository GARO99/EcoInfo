from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship

from Models.Base.Base_model import Base_Model

if TYPE_CHECKING:
    from Models.Company.company import Company


class Company_Type(Base_Model, table=True):
    name: str = Field(default=None, nullable=False, max_length= 100)

    companys: list["Company"] = Relationship(back_populates="company_type")