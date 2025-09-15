from typing import List
from uuid import UUID
from fastapi import HTTPException
from app.models.product import Product
from app.repos.product import ProductRepo
from app.schemas.product.request import ProductCreate
from app.schemas.product.response import ProductRead


class ProductService:
    def __init__(self, repo: ProductRepo):
        self.repo = repo

    async def create(self, product_data: ProductCreate) -> ProductRead:
        product = Product(**product_data.dict())
        await self.repo.create(product)
        return ProductRead.from_orm(product)

    async def get_by_id(self, product_id: UUID) -> ProductRead:
        product = await self.repo.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail=f"Product {product_id} not found")
        return ProductRead.from_orm(product)

    async def list(self) -> List[ProductRead]:
        products = await self.repo.list_all()
        return [ProductRead.from_orm(p) for p in products]

    async def get_by_ids(self, ids: List[UUID]) -> List[ProductRead]:
        products = await self.repo.get_by_ids(ids)
        return [ProductRead.from_orm(p) for p in products]
