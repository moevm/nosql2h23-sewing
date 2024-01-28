from fastapi import APIRouter, status, Request, HTTPException, Depends
from ..schemas.customer import RestCustomerRegister, RestCustomerLogin
from ...database.database import DatabaseService
from ...services.utils.jwt_processing import Auth

common_router = APIRouter(
    tags=["common"],
    responses={404: {"description": "Not found"}},
)


@common_router.post("/login")
async def login(request: Request, data: RestCustomerLogin):
    database: DatabaseService = request.app.state.database

    auth = Auth()
    user = await database.get_user(email=data.email)

    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Неверный e-mail!')
    if not auth.verify_password(data.password, user["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Неверный пароль')
    if user["status"] == "Need to approve":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Пожалуйста, дождитесь, пока с Вами свяжется менеджер.')
    if user["status"] == "Declined":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='К сожалению, ваша заявка была отклонена.')

    access_token = auth.create_token(data.email, user["role"])
    refresh_token = auth.create_refresh_token(data.email, user["role"])

    return {"access_token": access_token, "refresh_token": refresh_token, "role": user["role"]}
