from enum import StrEnum
from pydantic import BaseModel, ConfigDict
from typing import List
from uuid import UUID
from app.schemas.order_item.response import OrderItem


class OrderStatus(StrEnum):
    PENDING = "PENDING"
    PAID = "PAID"
    CANCELLED = "CANCELLED"


class OrderRead(BaseModel):
    id: UUID
    customer_id: UUID
    items: List[OrderItem]
    total_price: float
    status: OrderStatus

    model_config = ConfigDict(from_attributes=True)
