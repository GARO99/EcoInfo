from typing import Optional
import uuid
from pydantic import BaseModel, Field


class Product_schema(BaseModel):
    id: Optional[uuid.UUID] = Field(default=None, nullable=True)
    name: str = Field(default=None, nullable=False, max_length= 50)
    description: str = Field(default=None, nullable=False, max_length= 100)
    brand: str = Field(default=None, nullable=False, max_length= 50)
    product_category_id: uuid.UUID = Field(default=None, nullable=False)
    
    class Config:
        json_schema_extra = {
            "example":{
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "name": "Repelente De Plagas - Sns 209 Pesticida Concentrado",
                "description": "Repelente De Plagas - Sns 209 Pesticida Concentrado 1 Galón",
                "brand": "Sns",
                "product_category_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
            }
        }