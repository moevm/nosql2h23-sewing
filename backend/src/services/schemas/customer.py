from pydantic import BaseModel, EmailStr, Field, constr


class RestCustomerRegister(BaseModel):
    email: EmailStr = Field(description="New user email")
    password: constr(min_length=1, max_length=256) = Field(description="New user password")
    TIN: constr(min_length=1, max_length=256) = Field(description="New user password")
    name: constr(min_length=1, max_length=256) = Field(description="New user password")
    contact_person: constr(min_length=1, max_length=256) = Field(description="New user password")
    phone: constr(min_length=1, max_length=256) = Field(description="New user password")


class RestCustomerLogin(BaseModel):
    email: EmailStr = Field(description="Login e-mail")
    password: constr(min_length=1, max_length=256) = Field(description="Login password")
