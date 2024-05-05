from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship
from Models.Base.Base_model import Base_Model

if TYPE_CHECKING:
    from Models.Product.product import Product

class Product_category(Base_Model, table=True):
    name: str = Field(default=None, nullable=False, max_length= 50)

    products: list["Product"] = Relationship(back_populates="product_category")