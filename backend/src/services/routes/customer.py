from fastapi import APIRouter, status, Request, HTTPException
from ..schemas.customer import RestCustomerRegister, RestCustomerLogin
from backend.src.database.database import DatabaseService
from backend.src.services.utils.jwt_processing import Auth

customer_router = APIRouter(
    tags=["customer"],
    responses={404: {"description": "Not found"}},
)


@customer_router.post(
    path="/register",
    status_code=status.HTTP_201_CREATED,
    responses={400: {}, 401: {}, 403: {}},
)
async def register(request: Request, data: RestCustomerRegister):
    database: DatabaseService = request.app.state.database
    user = await database.get_customer(email=data.email)

    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exist",
        )

    user = await database.register_customer(
        email=data.email,
        password=data.password,
        TIN=data.TIN,
        name=data.name,
        contact_person=data.contact_person,
        phone=data.phone,
    )

    auth = Auth()
    access_token = auth.create_token(user["email"])
    refresh_token = auth.create_refresh_token(user["email"])
    return {"access_token": access_token, "refresh_token": refresh_token}


@customer_router.post("/login")
async def login(request: Request, data: RestCustomerLogin):
    database: DatabaseService = request.app.state.database

    auth = Auth()
    user = await database.get_customer(email=data.email)

    if user is None:
        return HTTPException(status_code=401, detail='Invalid email')
    if not auth.verify_password(data.password, user["hashed_password"]):
        return HTTPException(status_code=401, detail='Invalid password')

    access_token = auth.create_token(data.email)
    refresh_token = auth.create_refresh_token(data.email)

    return {"access_token": access_token, "refresh_token": refresh_token}
