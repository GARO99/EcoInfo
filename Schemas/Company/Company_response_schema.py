from typing import Optional
import uuid

from pydantic import BaseModel, Field

from Models.Company.company_type import Company_Type


class Company_Response_Schema(BaseModel):
    id: Optional[uuid.UUID] = Field(default=None, nullable=True)
    name: str = Field(nullable=False, max_length= 100)
    company_type_id: uuid.UUID = Field(default=None, nullable=False)
    company_type: Company_Type = Field(default=None, nullable=False)