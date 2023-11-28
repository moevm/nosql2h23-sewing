from starlette.middleware.cors import CORSMiddleware
from services.service import APIService
from database.database import DatabaseService

import uvicorn

# api = APIService(DatabaseService("postgresql+asyncpg://postgres:password@localhost:5432/your_dormitory"))
api = APIService(DatabaseService("mongodb://localhost:27017"))

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
    # init_db()
    uvicorn.run("main:api.app", port=3000, reload=True, workers=1)
