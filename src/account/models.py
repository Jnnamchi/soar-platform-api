import typing as ty
from datetime import datetime
from pydantic import BaseModel, EmailStr

from werkzeug.security import generate_password_hash


class UserOut(BaseModel):

    id: str
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    job_title: str
    phone: str
    is_active: bool
    role: ty.Literal['administrator', 'participant'] = 'administrator'


class UserIn(BaseModel):

    email: EmailStr
    password: str
    first_name: str
    last_name: str
    job_title: str
    phone: str
    is_active: bool = False
    role: ty.Literal['administrator', 'participant'] = 'administrator'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = self.email.lower()

    def hash_password(self):
        self.password = generate_password_hash(self.password)


class SignupRequestOut(BaseModel):

    id: str
    email: EmailStr
    created_at: datetime


class SignupRequestIn(BaseModel):

    email: EmailStr
    created_at: datetime


class TwoFARequestIn(BaseModel):

    user_id: str
    code: str
    created_at: datetime


class TwoFARequestOut(TwoFARequestIn):
    id: str


class UserInvitationIn(BaseModel):

    admin_id: str
    email: EmailStr
    created_at: datetime


class UserInvitationOut(UserInvitationIn):
    id: str


class ResetPasswordReqIn(BaseModel):

    email: EmailStr
    created_at: datetime


class ResetPasswordReqOut(ResetPasswordReqIn):
    id: str

