from pydantic import BaseModel, Field, constr


class RestModelLoad(BaseModel):
    name: str
    path_to_model: str


class RestAdminLogin(BaseModel):
    email: constr(min_length=1, max_length=256) = Field(description="Login e-mail")
    password: constr(min_length=1, max_length=256) = Field(description="Login password")


class RestManagerCreate(BaseModel):
    name: constr(min_length=1, max_length=256) = Field(description="Manager`s name that user sees")
    email: constr(min_length=1, max_length=256) = Field(description="Manager`s email")
    password: constr(min_length=1, max_length=256) = Field(description="Password")
    about: constr(min_length=1, max_length=256) = Field(description="Description")


class RestToken(BaseModel):
    token: str


class RestSettings(BaseModel):
    link_to_video: str
    width_of_video: int
    height_of_video: int


class RestApproveForm(BaseModel):
    id: int
    type: str


class RestModelUpdateForm(BaseModel):
    model_id: int
    name: str
    type: str
    status: int
    conflicts_to: str
    description: str
    color_count: int


class RestUserUpdateForm(BaseModel):
    user_id: int = Field(description="User ID")
    email: constr(min_length=1, max_length=64) = Field(description="User email")
    role: constr(min_length=1, max_length=32) = Field(description="User email")
    hashed_password: constr(min_length=1, max_length=512) = Field(description="User password")
    TIN: constr(min_length=1, max_length=16) = Field(description="User TIN")
    name: constr(min_length=1, max_length=64) = Field(description="User name")
    contact_person: constr(min_length=1, max_length=128) = Field(description="User contact_person")
    phone: constr(min_length=1, max_length=32) = Field(description="User phone")
    status: constr(min_length=1, max_length=32) = Field(description="User phone")
    about: constr(min_length=1, max_length=2048) = Field(description="User about")
