import datetime

from pydantic import BaseModel, EmailStr
from werkzeug.security import generate_password_hash


class UserResponse(BaseModel):
    id: str
    email: EmailStr
    first_name: str
    last_name: str
    role: str


class UserInput(BaseModel):

    email: EmailStr
    password: str
    first_name: str
    last_name: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = self.email.lower()
        self.password = generate_password_hash(self.password)


class UserLogin(BaseModel):

    email: EmailStr
    password: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = self.email.lower()


class TokenResponse(BaseModel):
    access_token: str


class SignupStart(BaseModel):

    email: EmailStr
    password: str
    first_name: str
    last_name: str
    phone: str
    company_name: str
    organization_size: str
    industry: str
    job_title: str


class TFASessionResponse(BaseModel):
    id: str
    created_at: datetime.datetime


class TFACodeRequest(BaseModel):
    code: str


class InviteUserRequest(BaseModel):
    email: EmailStr


class AcceptInvitation(BaseModel):

    invitation_id: str
    first_name: str
    last_name: str
    password: str


class ResetPasswordStart(BaseModel):
    email: EmailStr


class ResetPasswordFinish(BaseModel):
    password: str


