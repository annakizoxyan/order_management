from app.models import UUIDDocument


class Customer(UUIDDocument):
    name: str
    email: str

    class Settings:
        name = "customers"
