from pydantic import BaseModel, EmailStr, Field, constr


class RestCustomerRegister(BaseModel):
    email: EmailStr = Field(description="New user email")
    password: constr(min_length=1, max_length=256) = Field(description="New user password")
    TIN: constr(min_length=1, max_length=256) = Field(description="New user TIN")
    name: constr(min_length=1, max_length=256) = Field(description="New user name")
    contact_person: constr(min_length=1, max_length=256) = Field(description="New user contact_person")
    phone: constr(min_length=1, max_length=256) = Field(description="New user phone")


class RestCustomerLogin(BaseModel):
    email: EmailStr = Field(description="Login e-mail")
    password: constr(min_length=1, max_length=256) = Field(description="Login password")
