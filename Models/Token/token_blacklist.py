from sqlmodel import Field
from Models.Base.Base_model import Base_Model


class Token_blacklist(Base_Model, table=True):
    expires_token: str =  Field(default=None, nullable=False)