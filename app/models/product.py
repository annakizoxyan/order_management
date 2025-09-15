from app.models import UUIDDocument


class Product(UUIDDocument):
    name: str
    price: float

    class Settings:
        name = "products"
