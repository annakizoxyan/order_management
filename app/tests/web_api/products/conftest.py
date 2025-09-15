import pytest_asyncio
import pytest
from faker import Faker
from app.models import Product


@pytest.fixture(scope="session")
def faker():
    return Faker()


@pytest_asyncio.fixture
def product_payload(faker):
    return {
        "name": faker.word(),
        "price": round(faker.pyfloat(positive=True), 2),
    }


@pytest_asyncio.fixture
async def product(faker, init_test_db):
    product = Product(
        name=faker.word().capitalize(),
        price=faker.random_int(min=10, max=1000),
    )
    await product.insert()
    return product.dict()


@pytest_asyncio.fixture
async def products(faker, init_test_db):
    created = []
    for _ in range(3):
        product = Product(
            name=faker.word().capitalize(),
            price=faker.random_int(min=10, max=1000),
        )
        await product.insert()
        created.append(product.dict())
    return created

