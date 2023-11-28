import aiofiles as aiofiles
from fastapi import APIRouter, status, Request, UploadFile, File, Form
from ..schemas.admin import RestModelLoad
from typing import Annotated
from backend.src.database.database import DatabaseService

import os

admin_router = APIRouter(
    tags=["admin"],
    responses={404: {"description": "Not found"}},
)


@admin_router.post(
    path="/load_model",
    status_code=status.HTTP_201_CREATED,
    responses={400: {}, 401: {}, 403: {}},
)
async def load_model(request: Request, path_to_model: Annotated[str, Form()], file: UploadFile = File(...)):
    database: DatabaseService = request.app.state.database
    print(file.filename)
    print(path_to_model)
    async with aiofiles.open(f"../models/{path_to_model}/{file.filename}", 'wb') as out_file:
        content = await file.read()  # async read
        await out_file.write(content)  # async write
    return status.HTTP_201_CREATED

