import uuid
from datetime import datetime
from typing import Optional
from sqlmodel import DateTime, Field, SQLModel, func

class Base_Model(SQLModel):
    id: Optional[uuid.UUID] = Field(primary_key=True)
    created_at: datetime = Field(sa_type=DateTime(timezone=True), default=func.now())
    updated_at: datetime = Field(sa_type=DateTime(timezone=True), default=func.now(),sa_column_kwargs={"onupdate": func.now(), "nullable": True})

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.id:
            self.id = uuid.uuid4()