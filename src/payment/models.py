import datetime
import typing as ty
from decimal import Decimal
from pydantic import BaseModel, condecimal


class InitCheckout(BaseModel):
    created_by: str
    company_id: str
    amount: condecimal(max_digits=6, decimal_places=2, gt=Decimal(1), lt=Decimal(50000))
    success_url: str
    cancel_url: str


class InitPaymentResp(BaseModel):
    checkout_url: str


class Product(BaseModel):
    id: str
    name: str
    description: str
    price: int


class PaymentModel(BaseModel):
    id: ty.Optional[str]
    created_by: str
    company_id: str
    created_at: datetime.datetime
    status: ty.Literal['init', 'success', 'processing', 'failed'] = 'init'
    amount: int
    products: ty.List[Product]
    checkout_session_id: ty.Optional[str]


class PaymentQuery(BaseModel):
    created_by: ty.Optional[str]
    company_id: ty.Optional[str]


class PaymentsResponse(BaseModel):
    results: ty.List[PaymentModel]


class StripeCustomer(BaseModel):
    user_id: str
    customer_id: str
