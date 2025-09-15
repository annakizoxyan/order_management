from uuid import UUID
from pydantic import BaseModel, ConfigDict


class ProductRead(BaseModel):
    id: UUID
    name: str
    price: float

    model_config = ConfigDict(from_attributes=True)
