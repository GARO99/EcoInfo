from decimal import Decimal
from typing import Optional
import uuid
from pydantic import BaseModel, Field


class Store_schema(BaseModel):
    id: Optional[uuid.UUID] = Field(default=None, nullable=True)
    name: str = Field(default=None, nullable=False, max_length= 100)
    direction: str = Field(default=None, nullable=False, max_length= 100)
    latitude: Decimal = Field(default=None, nullable=False)
    longitude: Decimal = Field(default=None, nullable=False)
    company_id: uuid.UUID = Field(default=None, nullable=False)

    class Config:
        json_schema_extra = {
            "example":{
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "name": "Casa Colonial Tintal",
                "direction": "Cll 33 #22-9",
                "latitude": -4.897984,
                "longitude": 4.897984,
                "company_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
            }
        }