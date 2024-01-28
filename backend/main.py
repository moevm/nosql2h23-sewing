from starlette.middleware.cors import CORSMiddleware
from src.services.service import APIService
from src.database.database import DatabaseService

import uvicorn

api = APIService(DatabaseService("mongodb://lensiz:KVvI6xGIVoL6v4xb@82.202.173.204:27017/?retryWrites=true&w=majority"))

api.app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@api.app.get("/api/health")
async def root():
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run("main:api.app", port=3000, reload=True, workers=1)
