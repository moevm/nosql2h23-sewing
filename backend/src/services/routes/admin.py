import aiofiles as aiofiles
from fastapi import APIRouter, status, Request, UploadFile, File, Form
from typing import Annotated
from ...database.database import DatabaseService
from ..schemas.admin import RestToken, RestApproveForm
from ..utils.jwt_processing import Auth

import os

admin_router = APIRouter(
    tags=["admin"],
    responses={404: {"description": "Not found"}},
)
auth = Auth()


@admin_router.post(
    path="/load_model",
    status_code=status.HTTP_201_CREATED,
    responses={400: {}, 401: {}, 403: {}},
)
async def load_model(request: Request,
                     path_to_model: Annotated[str, Form()] = "",
                     name: Annotated[str, Form()] = "",
                     type_of_model: Annotated[str, Form()] = "",
                     description: Annotated[str, Form()] = "",
                     file: UploadFile = File(...)):
    database: DatabaseService = request.app.state.database

    print(name)
    print(type_of_model)
    print(description)
    print(path_to_model)
    if '/' in path_to_model:
        print(path_to_model.split("/"))
        for i in range(len(path_to_model.split("/"))):
            try:
                os.mkdir("../models/" + '/'.join(path_to_model.split("/")[:i + 1]))
            except FileExistsError as e:
                pass
    else:
        os.mkdir("../models/" + path_to_model)
    async with aiofiles.open(f"../models/{path_to_model}/{file.filename}", 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)

    database.load_model(
        model=file.filename,
        name=name,
        path_to_model=path_to_model,
        model_type=type_of_model,
        description=description
    )
    return status.HTTP_201_CREATED


@admin_router.post(
    path="/registration_applications",
    status_code=status.HTTP_200_OK,
    responses={400: {}, 401: {}, 403: {}},
)
async def registration_applications(request: Request, token: RestToken):
    database: DatabaseService = request.app.state.database
    if auth.decode_token(token.token)["role"] != "admin":
        return status.HTTP_403_FORBIDDEN
    return await database.get_registration_applications()


@admin_router.post(
    path="/approve_application",
    status_code=status.HTTP_200_OK,
    responses={400: {}, 401: {}, 403: {}},
)
async def approve_application(request: Request, form: RestApproveForm):
    database: DatabaseService = request.app.state.database
    if auth.decode_token(form.token)["role"] != "admin":
        return status.HTTP_403_FORBIDDEN
    if form.type == "customer":
        await database.approve_customer(form.id)
    elif form.type == "company":
        await database.approve_company(form.id)
    return status.HTTP_200_OK


@admin_router.post(
    path="/decline_application",
    status_code=status.HTTP_200_OK,
    responses={400: {}, 401: {}, 403: {}},
)
async def decline_application(request: Request, form: RestApproveForm):
    database: DatabaseService = request.app.state.database
    if auth.decode_token(form.token)["role"] != "admin":
        return status.HTTP_403_FORBIDDEN
    if form.type == "customer":
        await database.decline_customer(form.id)
    elif form.type == "company":
        await database.decline_customer(form.id)
    return status.HTTP_200_OK
