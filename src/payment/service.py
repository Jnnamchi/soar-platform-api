import uuid
import pytz
import datetime

from flask import current_app
from firebase_admin import auth

from .models import InitCheckout, Product, PaymentModel, StripeCustomer




def get_or_create_stripe_customer(user_id: str) -> StripeCustomer:
    """Lookup in firestore for customer and create if not exists"""
    stripe = current_app.config['STRIPE']
    db = current_app.config['FIRESTORE']

    user = auth.get_user(user_id)

    db_cust = db.collection(u'stripe_customers').where(u'user_id', u'==', user_id).get()
    if not db_cust:
        customer = stripe.Customer.create(email=user.email, name=user.display_name)
        cust_item = StripeCustomer(user_id=user_id, customer_id=customer.id)
        db.collection(u'stripe_customers').add(cust_item.dict())
    else:
        db_cust = db_cust[0]
        cust_item = StripeCustomer(**db_cust.to_dict())

    return cust_item


def create_checkout_session(data: InitCheckout):
    """Build order and init checkout and save data in db"""

    stripe = current_app.config['STRIPE']
    db = current_app.config['FIRESTORE']

    customer = get_or_create_stripe_customer(data.created_by)
    product = Product(
        id=str(uuid.uuid4()),
        name='Soar product',
        description='This is test Soar-Platform product.',
        price=int(data.amount * 100),
    )
    products = list()
    products.append(product)
    amount = sum([p.price for p in products])

    line_items = list()
    for p in products:
        stripe_product = stripe.Product.create(**p.dict(exclude={'price'}))
        price = stripe.Price.create(
            product=stripe_product.id,
            unit_amount=p.price,
            currency='usd'
        )
        line_items.append({
            'price': price.id,
            'quantity': 1,
        })

    session = stripe.checkout.Session.create(
        line_items=line_items,
        mode='payment',
        success_url=data.success_url,
        cancel_url=data.cancel_url,
        customer=customer.customer_id,
    )
    pmt_db_model = PaymentModel(
        created_by=data.created_by,
        company_id=data.company_id,
        created_at=datetime.datetime.now(tz=pytz.UTC).isoformat(),
        amount=amount,
        products=products,
        checkout_session_id=session.id,
    )
    db.collection(u'payments').add(pmt_db_model.dict())
    return session



