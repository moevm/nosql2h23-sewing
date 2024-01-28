from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes.company import company_router
from .routes.customer import customer_router
from .routes.admin import admin_router
from .routes.common import common_router
from ..database.database import DatabaseService


class APIService:
    def __init__(self, database: DatabaseService):
        self.debug = True
        self.app = FastAPI(
            title="API",
        )
        self.database = database

        origins = ["*"]
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=[""],
            allow_headers=[""],
        )
        self.app.state.database = database

        self.attach_routes()

    def attach_routes(self):
        api_router = APIRouter()
        api_router.prefix = "/api"

        api_router.include_router(router=company_router, prefix="/company", tags=["Company"])
        api_router.include_router(router=customer_router, prefix="/customer", tags=["Customer"])
        api_router.include_router(router=common_router, tags=["Common"])
        api_router.include_router(router=admin_router, prefix="/admin", tags=["Admin"])
        self.app.include_router(router=api_router)
