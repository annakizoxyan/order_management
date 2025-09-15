from uuid import UUID
from pydantic import BaseModel, EmailStr, ConfigDict


class CustomerRead(BaseModel):
    id: UUID
    name: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)
