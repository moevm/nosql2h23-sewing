from fastapi import APIRouter, status, Request, HTTPException
from ..schemas.customer import RestCustomerRegister, RestCustomerToken, RestCustomerModelSettings, RestLayout
from ...database.database import DatabaseService
from ...services.utils.jwt_processing import Auth

customer_router = APIRouter(
    tags=["customer"],
    responses={404: {"description": "Not found"}},
)
auth = Auth()


@customer_router.post(
    path="/register",
    status_code=status.HTTP_201_CREATED,
    responses={400: {}, 401: {}, 403: {}},
)
async def register(request: Request, data: RestCustomerRegister):
    database: DatabaseService = request.app.state.database
    user = await database.get_user(email=data.email)

    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ввёденный e-mail уже используется.",
        )

    await database.register_customer(
        email=data.email,
        password=data.password,
        TIN=data.TIN,
        name=data.name,
        contact_person=data.contact_person,
        phone=data.phone,
    )

    return status.HTTP_201_CREATED


@customer_router.post(path="/models")
async def get_models(request: Request, data: RestCustomerModelSettings):
    database: DatabaseService = request.app.state.database

    content = await database.get_models_by_settings(
        work=data.work,
        sex=data.sex,
        season=data.season
    )
    return list(content)


@customer_router.post(path="/profile")
async def get_models(request: Request, data: RestCustomerToken):
    database: DatabaseService = request.app.state.database

    decoded_data = auth.decode_token(data.token)
    if decoded_data["role"] == "customer":
        return await database.get_user(decoded_data["email"])
    return None


@customer_router.get(path="/get_translates")
async def get_translates(request: Request):
    database: DatabaseService = request.app.state.database
    return await database.get_translates()


@customer_router.post(path="/save_layout")
async def save_layout(request: Request, layout: RestLayout):
    database: DatabaseService = request.app.state.database
    decoded_user = auth.decode_token(layout.access_token)

    if decoded_user["role"] != "customer":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="У вас нет доступа. Только покупатель может создавать макет",
        )
    await database.save_layout(email=decoded_user["email"],
                               elements=layout.elements,
                               name=layout.name,
                               active_elements=layout.active_elements,
                               elements_color=layout.elements_color,
                               elements_to_models=layout.elements_to_models,
                               last_element_id=layout.last_element_id,
                               )
    return status.HTTP_200_OK
