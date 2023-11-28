from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes.company import company_router
from backend.src.database.database import DatabaseService


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
        self.app.include_router(router=api_router)
