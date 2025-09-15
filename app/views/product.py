from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from app.schemas.product.request import ProductCreate
from app.schemas.product.response import ProductRead
from app.services.product import ProductService
from app.core.containers import AppContainer

router = APIRouter()


@router.post("/", response_model=ProductRead)
@inject
async def create_product(
    product: ProductCreate,
    service: ProductService = Depends(Provide[AppContainer.product_service])
):
    return await service.create(product)


@router.get("/{product_id}", response_model=ProductRead)
@inject
async def get_product(
    product_id: UUID,
    service: ProductService = Depends(Provide[AppContainer.product_service])
):
    return await service.get_by_id(product_id)


@router.get("/", response_model=List[ProductRead])
@inject
async def list_products(
    service: ProductService = Depends(Provide[AppContainer.product_service])
):
    return await service.list()
