from uuid import UUID
from fastapi import HTTPException
from app.models.order import Order
from app.repos.base import BaseRepo


class OrderRepo(BaseRepo[Order]):
    def __init__(self):
        super().__init__(model=Order)

    async def update_status(self, order_id: UUID, status: str) -> Order:
        order = await self.get_by_id(order_id)
        if order is None:
            raise HTTPException(
                status_code=404,
                detail=f"Order {order_id} does not exist"
            )
        order.status = status
        await order.save()
        return order
