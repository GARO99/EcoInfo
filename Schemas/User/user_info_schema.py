from typing import Optional
import uuid
from pydantic import BaseModel, Field


class User_info_schema(BaseModel):
    id: Optional[uuid.UUID] = Field(primary_key=True)
    name: str = Field(default=None, nullable=False, max_length= 45)
    last_name: str = Field(default=None, nullable=False)
    email: str = Field(default=None, nullable=False, max_length= 100)
    
    class Config:
        json_schema_extra = {
            "example":{
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "name": "Santiago",
                "last_name": "Angel",
                "email": "example@example.com"
            }
        }