from decimal import Decimal
from typing import Optional
import uuid
from pydantic import BaseModel, Field

from Models.Company.company import Company


class Store_response_schema(BaseModel):
    id: Optional[uuid.UUID] = Field(default=None, nullable=True)
    name: str = Field(default=None, nullable=False, max_length= 100)
    direction: str = Field(default=None, nullable=False, max_length= 100)
    latitude: Decimal = Field(default=None, nullable=False)
    longitude: Decimal = Field(default=None, nullable=False)
    company_id: uuid.UUID = Field(default=None, nullable=False)
    company: Company = Field(default=None, nullable=False)