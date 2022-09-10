import typing as ty
from pydantic import BaseModel


class EmailTemplate(BaseModel):

    name: str
    subj: str
    message: str
    html: ty.Optional[str]
