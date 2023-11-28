from typing import Optional

from pydantic import BaseModel


class ModelInSchema(BaseModel):
    path_to_model: str
