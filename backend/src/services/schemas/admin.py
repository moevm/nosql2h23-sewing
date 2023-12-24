from pydantic import BaseModel


class RestModelLoad(BaseModel):
    name: str
    path_to_model: str


class RestToken(BaseModel):
    token: str


class RestApproveForm(BaseModel):
    id: int
    type: str
    token: str
