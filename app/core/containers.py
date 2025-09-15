from dependency_injector import containers, providers
from fastapi import FastAPI
from app.core.config import EnvSecrets
from app.repos.customer import CustomerRepo
from app.repos.order import OrderRepo
from app.repos.product import ProductRepo
from app.services.customer import CustomerService
from app.services.order import OrderService
from app.services.product import ProductService


class AppContainer(containers.DeclarativeContainer):
    app_factory = providers.Factory(FastAPI, title="Order Management", version="0.1.0")
    config = providers.Singleton(EnvSecrets)
    customer_repo = providers.Factory(CustomerRepo)
    product_repo = providers.Factory(ProductRepo)
    order_repo = providers.Factory(OrderRepo)

    customer_service = providers.Factory(
        CustomerService,
        repo=customer_repo
    )
    product_service = providers.Factory(
        ProductService,
        repo=product_repo
    )
    order_service = providers.Factory(
        OrderService,
        repo=order_repo,
    )


app_container = AppContainer()
