from pydantic import BaseModel, Field


class Suggestion_schema(BaseModel):
    email: str = Field(default=None, nullable=False, max_length= 100)
    suggest_text: str = Field(default=None, nullable=False)