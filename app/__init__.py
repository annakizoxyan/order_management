from fastapi import APIRouter, FastAPI
from app.core.db import init_db
from app.core.containers import app_container
from app.views.order import router as order_router
from app.views.product import router as product_router
from app.views.customer import router as customer_router

api_wire = [
    "app.views.customer",
    "app.views.product",
    "app.views.order"
]


def get_router() -> APIRouter:
    router = APIRouter()
    router.include_router(customer_router, prefix="/customers", tags=["customers"])
    router.include_router(product_router, prefix="/products", tags=["products"])
    router.include_router(order_router, prefix="/orders", tags=["orders"])
    return router


def create_app() -> FastAPI:
    app_container.wire(packages=api_wire)
    app = app_container.app_factory()
    router = get_router()
    app.include_router(router)

    @app.on_event("startup")
    async def on_startup():
        await init_db()

    return app
