from typing import List
from uuid import UUID
from pydantic import BaseModel
from app.schemas.order.response import OrderStatus
from app.schemas.order_item.response import OrderItem


class OrderCreate(BaseModel):
    customer_id: UUID
    items: List[OrderItem]


class OrderUpdateStatus(BaseModel):
    status: OrderStatus
