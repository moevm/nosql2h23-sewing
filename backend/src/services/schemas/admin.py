from pydantic import BaseModel


class RestModelLoad(BaseModel):
    path_to_model: str
