from pydantic import BaseModel, Field
from uuid import UUID


class OrderItem(BaseModel):
    product_id: UUID
    quantity: int = Field(default=1, ge=1)
