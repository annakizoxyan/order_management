from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from app.schemas.customer.request import CustomerCreate
from app.schemas.customer.response import CustomerRead
from app.services.customer import CustomerService
from app.core.containers import AppContainer

router = APIRouter()


@router.post("/", response_model=CustomerRead)
@inject
async def create_customer(
    customer: CustomerCreate,
    service: CustomerService = Depends(Provide[AppContainer.customer_service])
):
    return await service.create(customer)


@router.get("/{customer_id}", response_model=CustomerRead)
@inject
async def get_customer(
    customer_id: UUID,
    service: CustomerService = Depends(Provide[AppContainer.customer_service])
):
    return await service.get_by_id(customer_id)


@router.get("/", response_model=List[CustomerRead])
@inject
async def list_customers(
    service: CustomerService = Depends(Provide[AppContainer.customer_service])
):
    return await service.list()
