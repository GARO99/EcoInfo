from typing import Optional
import uuid
from pydantic import BaseModel, Field

from Models.Product.product_category import Product_category


class Product_response_schema(BaseModel):
    id: Optional[uuid.UUID] = Field(default=None, nullable=True)
    name: str = Field(default=None, nullable=False, max_length= 50)
    description: str = Field(default=None, nullable=False, max_length= 100)
    brand: str = Field(default=None, nullable=False, max_length= 50)
    product_category_id: uuid.UUID = Field(default=None, nullable=False)
    product_category: Product_category = Field(default=None, nullable=False)