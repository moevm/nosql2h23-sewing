from pydantic import BaseModel


class RestModelLoad(BaseModel):
    name: str
    path_to_model: str
