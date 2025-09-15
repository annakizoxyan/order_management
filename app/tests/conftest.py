from app.asgi import app as asgi_app
import pytest
from fastapi import FastAPI
from app.core.config import get_env_secrets
import pytest_asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models import Customer, Product, Order

env = get_env_secrets()
MONGO_URI = env.build_mongo_uri()


@pytest.fixture
def app() -> FastAPI:
    return asgi_app


@pytest_asyncio.fixture
async def init_test_db():
    client = AsyncIOMotorClient(MONGO_URI)
    db = client[env.MONGO_DB + "_test"]

    await init_beanie(database=db, document_models=[Customer, Product, Order])

    collections = await db.list_collection_names()
    for coll in collections:
        await db.drop_collection(coll)

    yield db

    collections = await db.list_collection_names()
    for coll in collections:
        await db.drop_collection(coll)

    client.close()


@pytest_asyncio.fixture
async def client(init_test_db, app):
    from httpx import AsyncClient
    async with AsyncClient(app=app, base_url="http://test") as c:
        yield c
