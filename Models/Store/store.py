from decimal import Decimal
from typing import TYPE_CHECKING, Optional
import uuid
from sqlmodel import Field, Relationship

from Models.Base.Base_model import Base_Model
from Models.Company.company import Company

if TYPE_CHECKING:
    from Models.Product.product_store import Product_store


class Store(Base_Model, table=True):
    name: str = Field(default=None, nullable=False, max_length= 100)
    direction: str = Field(default=None, nullable=False, max_length= 100)
    latitude: Decimal =  Field(default=None, nullable=False)
    longitude: Decimal =  Field(default=None, nullable=False)
    company_id: uuid.UUID = Field(default=None, nullable=False, foreign_key="company.id")

    company: Optional[Company] = Relationship(back_populates="stores")
    product_stores: list["Product_store"] = Relationship(back_populates="store")