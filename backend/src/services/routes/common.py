from fastapi import APIRouter, status, Request, HTTPException, Depends
from ..schemas.customer import RestCustomerRegister, RestCustomerLogin
from ...database.database import DatabaseService
from ...services.utils.jwt_processing import Auth

common_router = APIRouter(
    tags=["common"],
    responses={404: {"description": "Not found"}},
)


@common_router.post(
    path="/registration_applications",
    status_code=status.HTTP_200_OK,
    responses={400: {}, 401: {}, 403: {}},
)
async def registration_applications(request: Request, data: RestCustomerRegister):
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