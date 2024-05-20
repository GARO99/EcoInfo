from sqlmodel import Field
from Models.Base.Base_model import Base_Model

class Plant(Base_Model, table=True):
    name: str = Field(default=None, nullable=False, max_length= 200)
    nom_scientifique: str = Field(default=None, nullable=False, max_length= 200)
    description: str = Field(default=None, nullable=False, max_length= 1000)