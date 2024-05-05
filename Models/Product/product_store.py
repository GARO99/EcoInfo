from decimal import Decimal
from typing import Optional
import uuid

from sqlmodel import Field, Relationship
from Models.Base.Base_model import Base_Model
from Models.Product.product import Product
from Models.Store.store import Store


class Product_store(Base_Model, table=True):
    price: Decimal =  Field(default=None, nullable=False)
    product_id: uuid.UUID = Field(default=None, nullable=False, foreign_key="product.id")
    store_id: uuid.UUID = Field(default=None, nullable=False, foreign_key="store.id")
    
    product: Optional[Product] = Relationship(back_populates="product_stores")
    store: Optional[Store] = Relationship(back_populates="product_stores")