from typing import List
from uuid import UUID
from fastapi import HTTPException
from app.models.order import Order
from app.schemas.order.request import OrderCreate
from app.schemas.order.response import OrderRead, OrderStatus
from app.services.product import ProductService
from app.services.customer import CustomerService
from app.repos.order import OrderRepo


class OrderService:
    def __init__(self, repo: OrderRepo):
        self.repo = repo

    async def create(
        self,
        order_create: OrderCreate,
        product_service: ProductService,
        customer_service: CustomerService,
    ) -> OrderRead:
        try:
            await customer_service.get_by_id(order_create.customer_id)
        except HTTPException as e:
            if e.status_code == 404:
                raise HTTPException(
                    status_code=422,
                    detail=f"Customer {order_create.customer_id} does not exist"
                )
            raise
        product_ids = [item.product_id for item in order_create.items]
        products = await product_service.get_by_ids(product_ids)
        existing_ids = {p.id for p in products}

        missing = [pid for pid in product_ids if pid not in existing_ids]
        if missing:
            raise HTTPException(status_code=422, detail=f"Products not found: {missing}")

        price_map = {p.id: p.price for p in products}
        order = Order(**order_create.dict())
        order.set_price_map(price_map)

        created_order = await self.repo.create(order)
        return OrderRead.from_orm(created_order)

    async def get_by_id(self, order_id: UUID) -> OrderRead:
        order = await self.repo.get_by_id(order_id)
        if not order:
            raise HTTPException(status_code=404, detail=f"Order {order_id} not found")
        return OrderRead.from_orm(order)

    async def list(self) -> List[OrderRead]:
        orders = await self.repo.list_all()
        return [OrderRead.from_orm(o) for o in orders]

    async def update_status(self, order_id: UUID, status: str) -> OrderRead:
        order = await self.get_by_id(order_id)

        if order.status == status:
            return OrderRead.from_orm(order)

        if order.status == OrderStatus.PENDING and status in [OrderStatus.PAID, OrderStatus.CANCELLED]:
            order.status = status
        else:
            raise HTTPException(
                status_code=422,
                detail=f"Cannot change status from {order.status} to {status}"
            )
        await Order(**order.dict()).save()

        return OrderRead.from_orm(order)
