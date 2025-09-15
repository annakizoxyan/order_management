from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from app.schemas.order.request import OrderCreate, OrderUpdateStatus
from app.schemas.order.response import OrderRead
from app.services.customer import CustomerService
from app.services.order import OrderService
from app.core.containers import AppContainer
from app.services.product import ProductService

router = APIRouter()


@router.post("/", response_model=OrderRead)
@inject
async def create_order(
    order_create: OrderCreate,
    service: OrderService = Depends(Provide[AppContainer.order_service]),
    product_service: ProductService = Depends(Provide[AppContainer.product_service]),
    customer_service: CustomerService = Depends(Provide[AppContainer.customer_service]),
):
    return await service.create(order_create, product_service, customer_service)


@router.get("/{order_id}", response_model=OrderRead)
@inject
async def get_order(
    order_id: UUID,
    service: OrderService = Depends(Provide[AppContainer.order_service])
):
    return await service.get_by_id(order_id)


@router.get("/", response_model=List[OrderRead])
@inject
async def list_orders(
    service: OrderService = Depends(Provide[AppContainer.order_service])
):
    return await service.list()


@router.patch("/{order_id}/status", response_model=OrderRead)
@inject
async def update_order_status(
    order_id: UUID,
    update: OrderUpdateStatus,
    service: OrderService = Depends(Provide[AppContainer.order_service])
):
    return await service.update_status(order_id, update.status)
