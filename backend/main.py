from starlette.middleware.cors import CORSMiddleware
from src.services.service import APIService
from src.database.database import DatabaseService

import uvicorn

api = APIService(DatabaseService("mongodb://filipp:creator_of_the_world_1232122@localhost:27017/?retryWrites=true&w=majority"))

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
