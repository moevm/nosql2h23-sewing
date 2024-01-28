from pydantic import BaseModel, EmailStr, Field, constr


class RestCompanyRegister(BaseModel):
    email: EmailStr = Field(description="New user email")
    password: constr(min_length=1, max_length=256) = Field(description="New user password")
    TIN: constr(min_length=1, max_length=256) = Field(description="New user password")
    name: constr(min_length=1, max_length=256) = Field(description="New user password")
    contact_person: constr(min_length=1, max_length=256) = Field(description="New user password")
    phone: constr(min_length=1, max_length=256) = Field(description="New user password")


class RestCompanyLogin(BaseModel):
    email: EmailStr = Field(description="Login e-mail")
    password: constr(min_length=1, max_length=256) = Field(description="Login password")


class RestCompanyToken(BaseModel):
    token: constr(min_length=1, max_length=512) = Field(description="Access token")
