from sqlmodel import Field
from Models.Base.Base_model import Base_Model


class Suggestion(Base_Model, table=True):
    email: str = Field(default=None, nullable=False, max_length= 100)
    suggest_text: str = Field(default=None, nullable=False)