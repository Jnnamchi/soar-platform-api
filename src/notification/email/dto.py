from typing import Optional
from pydantic import BaseModel


class EmailTemplate(BaseModel):

    name: str
    subj: str
    message: str
    html: Optional[str]
