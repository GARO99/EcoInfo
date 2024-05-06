from typing import Optional
import uuid
from pydantic import BaseModel, Field


class Product_category_schema(BaseModel):
    id: Optional[uuid.UUID] = Field(default=None, nullable=True)
    name: str = Field(default=None, nullable=False, max_length= 50)
    
    class Config:
        json_schema_extra = {
            "example":{
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "name": "Pesticida",
            }
        }