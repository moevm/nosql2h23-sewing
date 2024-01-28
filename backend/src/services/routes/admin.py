import aiofiles as aiofiles
from fastapi import APIRouter, status, Request, UploadFile, File, Form, HTTPException
from typing import Annotated
from ...database.database import DatabaseService
from ..schemas.admin import RestApproveForm, RestModelUpdateForm, RestAdminLogin, RestManagerCreate, RestSettings, \
    RestUserUpdateForm
from ..utils.jwt_processing import Auth

import os

admin_router = APIRouter(
    tags=["admin"],
    responses={404: {"description": "Not found"}},
)


@admin_router.post(
    path="/login"
)
async def login(request: Request, form: RestAdminLogin):
    database: DatabaseService = request.app.state.database
    auth = Auth()

    if form.email == "admin" and form.password == "admin":

        access_token = auth.create_token(form.email, "admin")
        refresh_token = auth.create_refresh_token(form.email, "admin")

        return {"access_token": access_token, "refresh_token": refresh_token, "role": "admin"}
    else:
        manager = database.get_manager(form.email)
        if auth.verify_password(form.password, manager["hashed_password"]):
            access_token = auth.create_token(form.email, "manager")
            refresh_token = auth.create_refresh_token(form.email, "manager")
            return {"access_token": access_token, "refresh_token": refresh_token, "role": "manager"}
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Неверные данные"
    )


@admin_router.post(
    path="/create_manager",
    status_code=status.HTTP_201_CREATED,
    responses={400: {}, 401: {}, 403: {}},
)
async def create_manager(request: Request, form: RestManagerCreate):
    database: DatabaseService = request.app.state.database

    await database.create_manager(
        email=form.email,
        name=form.name,
        password=form.password,
        about=form.about,
    )
    return status.HTTP_201_CREATED


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

    if '/' in path_to_model:
        for i in range(len(path_to_model.split("/"))):
            try:
                os.mkdir(os.getcwd() + "/models/" + '/'.join(path_to_model.split("/")[:i + 1]))
            except FileExistsError as e:
                pass
    else:
        try:
            os.mkdir(os.getcwd() + "/models/" + path_to_model)
        except FileExistsError as e:
            pass

    async with aiofiles.open(os.getcwd() + f"/models/{path_to_model}/{file.filename}", 'wb') as out_file:
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


@admin_router.get(
    path="/registration_applications",
    status_code=status.HTTP_200_OK,
    responses={400: {}, 401: {}, 403: {}},
)
async def registration_applications(request: Request):
    database: DatabaseService = request.app.state.database
    return await database.get_registration_applications()


@admin_router.post(
    path="/approve_application",
    status_code=status.HTTP_200_OK,
    responses={400: {}, 401: {}, 403: {}},
)
async def approve_application(request: Request, form: RestApproveForm):
    database: DatabaseService = request.app.state.database
    # if auth.decode_token(form.token)["role"] != "admin":
    #     return status.HTTP_403_FORBIDDEN
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
    # if auth.decode_token(form.token)["role"] != "admin":
    #     return status.HTTP_403_FORBIDDEN
    if form.type == "customer":
        await database.decline_customer(form.id)
    elif form.type == "company":
        await database.decline_company(form.id)
    return status.HTTP_200_OK


@admin_router.get(path="/models")
async def get_models(request: Request):
    database: DatabaseService = request.app.state.database
    return list(await database.get_all_models())


@admin_router.post(path="/customers")
async def customers(request: Request, find_options: dict = None):
    database: DatabaseService = request.app.state.database

    page = find_options["page"]
    limit = find_options["limit"]
    find_options = find_options["find_options"]
    find_options["status"] = {"$ne": "Need to approve"}

    return {"users_count": await database.customers_count(find_options),
            "users": list(await database.customers(
                page=page,
                limit=limit,
                find_options=find_options,
            ))}


@admin_router.get(path="/customers/{user_id}")
async def get_customer(request: Request, user_id):
    database: DatabaseService = request.app.state.database
    return await database.get_customer(user_id)


@admin_router.post(path="/update_user")
async def get_model_by_id(request: Request, form: RestUserUpdateForm):
    database: DatabaseService = request.app.state.database
    database.update_user_text_fields(user_id=form.user_id,
                                     email=form.email,
                                     role=form.role,
                                     TIN=form.TIN,
                                     name=form.name,
                                     contact_person=form.contact_person,
                                     phone=form.phone,
                                     status=form.status,
                                     about=form.about,
                                     )
    return status.HTTP_200_OK


@admin_router.post(path="/companies")
async def companies(request: Request, find_options: dict = None):
    database: DatabaseService = request.app.state.database

    page = find_options["page"]
    limit = find_options["limit"]
    find_options = find_options["find_options"]
    find_options["status"] = {"$ne": "Need to approve"}

    return {"users_count": await database.companies_count(find_options),
            "users": list(await database.companies(
                page=page,
                limit=limit,
                find_options=find_options,
            ))}


@admin_router.get(path="/companies/{user_id}")
async def get_company(request: Request, user_id):
    database: DatabaseService = request.app.state.database

    return await database.get_company(user_id)


@admin_router.get(path="/settings")
async def get_settings(request: Request):
    database: DatabaseService = request.app.state.database
    return await database.get_settings()


@admin_router.post(path="/update_settings")
async def update_settings(request: Request, settings: RestSettings):
    database: DatabaseService = request.app.state.database
    await database.update_settings(
        link_to_video=settings.link_to_video,
        width_of_video=settings.width_of_video,
        height_of_video=settings.height_of_video
    )


@admin_router.get(path="/model/{model_id}")
async def get_model_by_id(request: Request, model_id):
    database: DatabaseService = request.app.state.database
    return await database.get_model_by_id(model_id)


@admin_router.post(path="/update_model/")
async def get_model_by_id(request: Request, form: RestModelUpdateForm):
    database: DatabaseService = request.app.state.database
    conflicts = [int(i.strip()) for i in form.conflicts_to.split(",")] if form.conflicts_to else []
    database.update_model_text_fields(model_id=form.model_id,
                                      name=form.name,
                                      conflicts_to=conflicts,
                                      status=form.status,
                                      color_count=form.color_count,
                                      model_type=form.type,
                                      description=form.description,
                                      )
    return status.HTTP_200_OK
