from pydantic import BaseModel, Field


class Sign_in_schema(BaseModel):
    email: str = Field(default=None, nullable=False, max_length= 100)
    password: str = Field(default=None, nullable=False)
    
    class Config:
        json_schema_extra = {
            "example":{
                "email": "example@example.com",
                "password": "217d2c34d529d04d84d09df19e7efd63fa2d619d21e4941536450f569cffd40b",
            }
        }