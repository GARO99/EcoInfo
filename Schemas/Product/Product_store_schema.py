from decimal import Decimal
from typing import Optional
import uuid
from pydantic import BaseModel, Field


class Product_store_schema(BaseModel):
    id: Optional[uuid.UUID] = Field(default=None, nullable=True)
    price: Decimal =  Field(default=None, nullable=False)
    product_id: uuid.UUID = Field(default=None, nullable=False)
    store_id: uuid.UUID = Field(default=None, nullable=False)
    
    class Config:
        json_schema_extra = {
            "example":{
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "price": 3000,
                "product_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "store_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
            }
        }