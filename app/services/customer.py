from typing import List
from uuid import UUID
from fastapi import HTTPException
from app.models.customer import Customer
from app.repos.customer import CustomerRepo
from app.schemas.customer.request import CustomerCreate
from app.schemas.customer.response import CustomerRead


class CustomerService:
    def __init__(self, repo: CustomerRepo):
        self.repo = repo

    async def create(self, customer_data: CustomerCreate) -> CustomerRead:
        customer = Customer(**customer_data.dict())
        await self.repo.create(customer)
        return CustomerRead.from_orm(customer)

    async def get_by_id(self, customer_id: UUID) -> CustomerRead:
        customer = await self.repo.get_by_id(customer_id)
        if not customer:
            raise HTTPException(
                status_code=404,
                detail=f"Customer {customer_id} not found"
            )
        return CustomerRead.from_orm(customer)

    async def list(self) -> List[CustomerRead]:
        customers = await self.repo.list_all()
        return [CustomerRead.from_orm(c) for c in customers]
