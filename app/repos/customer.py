from app.models.customer import Customer
from app.repos.base import BaseRepo


class CustomerRepo(BaseRepo[Customer]):
    def __init__(self):
        super().__init__(model=Customer)
