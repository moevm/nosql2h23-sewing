from pydantic import BaseModel, EmailStr, Field, constr
from typing import Dict, List, Any


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


class RestCustomerModelSettings(BaseModel):
    work: constr(min_length=1, max_length=64) = Field(description="Model work")
    sex: constr(min_length=1, max_length=64) = Field(description="Model sex")
    season: constr(min_length=1, max_length=64) = Field(description="Model season")


class RestCustomerToken(BaseModel):
    token: constr(min_length=1, max_length=512) = Field(description="Access token")


class RestLayout(BaseModel):
    access_token: constr(min_length=1, max_length=512) = Field(description="User`s token")
    name: constr(min_length=1, max_length=64) = Field(description="Layout name")
    elements: Dict[str, str | int] = Field(description="Elements")
    elements_color: Dict[str, List[str | int]] = Field(description="Elements")
    active_elements: Dict[str, str | int] = Field(description="Elements")
    elements_to_models: Dict[str, int | str] = Field(description="Elements")
    last_element_id: int = Field(description="Elements")
