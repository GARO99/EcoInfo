from typing import TYPE_CHECKING, Optional
import uuid
from sqlmodel import Field, Relationship
from Models.Base.Base_model import Base_Model
from Models.Product.product_category import Product_category

if TYPE_CHECKING:
    from Models.Product.product_store import Product_store


class Product(Base_Model, table=True):
    name: str = Field(default=None, nullable=False, max_length= 50)
    description: str = Field(default=None, nullable=False, max_length= 100)
    brand: str = Field(default=None, nullable=False, max_length= 50)
    product_category_id: uuid.UUID = Field(default=None, nullable=False, foreign_key="product_category.id")

    product_category: Optional[Product_category] = Relationship(back_populates="products")
    product_stores: list["Product_store"] = Relationship(back_populates="product")