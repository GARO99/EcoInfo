from pydantic import BaseModel, Field


class token_schema(BaseModel):
    access_token: str = Field(default=None, nullable=False)
    token_type: str = Field(default="bearer", nullable=False)
    
    class Config:
        json_schema_extra = {
            "example":{
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
                "token_type": "bearer"
            }
        }