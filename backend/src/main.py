import uvicorn
from fastapi import FastAPI, status, UploadFile, File
from starlette.middleware.cors import CORSMiddleware

from schemas.admin import ModelInSchema

from database import load_model

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=[""],
)


@app.get('/api/health')
async def health_check():
    return status.HTTP_200_OK


@app.post("/api/admin/load_model")
async def upload_model(ModelInSchema, file: UploadFile = File(...)):
    print(1)
    print(ModelInSchema.path_to_model)
    print(file)
    load_model(model=file, path_to_model=ModelInSchema.path_to_model)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8081, reload=True, workers=1)
