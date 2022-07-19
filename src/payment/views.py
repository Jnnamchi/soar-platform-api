import logging
import json
from flask import Blueprint, jsonify, current_app, request
from flask_pydantic import validate
from firebase_admin.firestore import firestore

from .models import InitCheckout, InitPaymentResp, PaymentQuery, PaymentsResponse
from .service import create_checkout_session
from .whooks.manager import WHookManager, WHookError


logger = logging.getLogger(__name__)

pmt = Blueprint('payment', __name__, url_prefix='/payment')


@pmt.route('/checkout', methods=['POST'])
@validate()
def init_checkout(body: InitCheckout):
    """Init checkout session from Stripe."""

    try:
        session = create_checkout_session(body)
    except Exception as e:
        logger.error(e)
        return jsonify({'error': str(e)}), 400

    return InitPaymentResp(checkout_url=session.url)


@pmt.route('/list', methods=['GET'])
@validate()
def get_payments(query: PaymentQuery):
    """Get payments."""

    db = current_app.config['FIRESTORE']

    user_id = query.created_by
    company_id = query.company_id

    m_query = db.collection(u'payments')
    if user_id:
        m_query = m_query.where(u'created_by', u'==', user_id)
    if company_id:
        m_query = m_query.where(u'company_id', u'==', company_id)

    m_query = m_query.order_by(u'created_at', direction=firestore.Query.DESCENDING)
    payments = []
    for row in m_query.stream():
        d = row.to_dict()
        d.update({'id': row.id})
        payments.append(d)

    return PaymentsResponse(results=payments)


@pmt.route('/webhook', methods=['POST'])
def webhook():
    """Stripe webhooks handler."""

    wh_secret = current_app.config['STRIPE_WHOOK_SECRET']
    stripe = current_app.config['STRIPE']
    payload = request.data

    sig_header = request.headers.get('stripe-signature')
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, wh_secret)
        whook = WHookManager.create(event)
        whook.handle()
        return jsonify(success=True)
    except stripe.error.SignatureVerificationError as e:
        logger.error('⚠️  Webhook signature verification failed.' + str(e))
        return jsonify(success=False)
    except WHookError as e:
        logger.error('⚠️  Webhook error: ' + str(e))
        return jsonify(success=False)



