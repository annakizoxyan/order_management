from typing import List
from uuid import UUID
from beanie import before_event, Insert
from pydantic import Field
from app.models import UUIDDocument
from app.schemas.order.response import OrderStatus
from app.schemas.order_item.response import OrderItem


class Order(UUIDDocument):
    customer_id: UUID
    items: List[OrderItem]
    total_price: float = Field(default=0.0)
    status: OrderStatus = Field(default=OrderStatus.PENDING)

    @before_event(Insert)
    async def compute_total(self):
        if not hasattr(self, "_price_map"):
            self.total_price = 0.0
            return
        self.total_price = sum(
            item.quantity * self._price_map[item.product_id] for item in self.items
        )

    def set_price_map(self, price_map: dict[UUID, float]):
        self._price_map = price_map

    class Settings:
        name = "orders"
