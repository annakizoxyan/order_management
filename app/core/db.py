from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.core.config import get_env_secrets
from app.models import Customer, Order, Product


async def init_db():
    env = get_env_secrets()
    mongo_uri = env.build_mongo_uri()

    client = AsyncIOMotorClient(mongo_uri)
    db = client[env.MONGO_DB]

    await init_beanie(database=db, document_models=[Customer, Product, Order])
