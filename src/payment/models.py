import datetime
from decimal import Decimal
from typing import Literal
from pydantic import BaseModel, validator, condecimal


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
    id: str | None
    created_by: str
    company_id: str
    created_at: datetime.datetime
    status: Literal['init', 'success', 'processing', 'failed'] = 'init'
    amount: int
    products: list[Product]
    checkout_session_id: str | None


class PaymentQuery(BaseModel):
    created_by: str | None
    company_id: str | None


class PaymentsResponse(BaseModel):
    results: list[PaymentModel]


class StripeCustomer(BaseModel):
    user_id: str
    customer_id: str
