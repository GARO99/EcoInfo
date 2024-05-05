from sqlmodel import Field
from Models.Base.Base_model import Base_Model


class User(Base_Model, table=True):
    name: str = Field(default=None, nullable=False, max_length= 45)
    last_name: str = Field(default=None, nullable=False)
    email: str = Field(default=None, nullable=False, max_length= 100)
    password: str = Field(default=None, nullable=False, max_length= 64)