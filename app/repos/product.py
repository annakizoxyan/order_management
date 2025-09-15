from app.models.product import Product
from app.repos.base import BaseRepo


class ProductRepo(BaseRepo[Product]):
    def __init__(self):
        super().__init__(model=Product)
