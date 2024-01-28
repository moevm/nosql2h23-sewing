from fastapi import APIRouter, status, Request, HTTPException
from ...services.schemas.company import RestCompanyToken, RestCompanyRegister
from ...database.database import DatabaseService
from ...services.utils.jwt_processing import Auth

company_router = APIRouter(
    tags=["company"],
    responses={404: {"description": "Not found"}},
)
auth = Auth()


@company_router.post(
    path="/register",
    status_code=status.HTTP_201_CREATED,
    responses={400: {}, 401: {}, 403: {}},
)
async def register(request: Request, data: RestCompanyRegister):
    database: DatabaseService = request.app.state.database
    user = await database.get_user(email=data.email)

    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ввёденный e-mail уже используется.",
        )

    await database.register_company(
        email=data.email,
        password=data.password,
        TIN=data.TIN,
        name=data.name,
        contact_person=data.contact_person,
        phone=data.phone,
    )

    return status.HTTP_201_CREATED


@company_router.post(path="/profile")
async def get_models(request: Request, data: RestCompanyToken):
    database: DatabaseService = request.app.state.database

    decoded_data = auth.decode_token(data.token)
    if decoded_data["role"] == "company":
        return await database.get_user(decoded_data["email"])
    return None
