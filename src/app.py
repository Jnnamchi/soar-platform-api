import os
from pathlib import Path

from flask import Flask
from flask import jsonify
from werkzeug.exceptions import HTTPException
from flask_cors import CORS

import stripe

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from libs.zoom import ZoomAPiClient, ZoomS2SOAuth, ZoomError

from soar.routes import soar
from zoom.views import zoom
from payment.views import pmt


def init_firestore(application: Flask):
    cred_path = Path() / 'credentials.json'
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)
    application.config['FIRESTORE'] = firestore.client()


def init_zoom_api(application: Flask):
    account_id = os.getenv('ZOOM_ACCOUNT_ID', None)
    client_id = os.getenv('ZOOM_CLIENT_ID', None)
    secret = os.getenv('ZOOM_CLIENT_SECRET', None)

    if not all([account_id, client_id, secret]):
        raise ZoomError(message='Zoom credentials not found in ENV variables')

    auth = ZoomS2SOAuth(client_id, secret, account_id)
    application.config['ZOOM_API'] = ZoomAPiClient(auth)


def init_stripe(application: Flask):
    key = os.getenv('STRIPE_API_KEY', None)
    whook_secret = os.getenv('STRIPE_WHOOK_SECRET', None)

    if not all([key, whook_secret]):
        raise Exception('STRIPE_API_KEY or STRIPE_WHOOK_SECRET not found in ENV variables')

    stripe.api_key = key
    application.config['STRIPE'] = stripe
    application.config['STRIPE_WHOOK_SECRET'] = whook_secret


def create_app() -> Flask:
    application = Flask(__name__)

    with application.app_context():
        init_firestore(application)
        init_zoom_api(application)
        init_stripe(application)

    CORS(
        application,
        origins=[
            'http://localhost:3000',
            'http://127.0.0.1:3000',
            'http://localhost:8080',
            'http://127.0.0.1:8080',
            'http://91.144.161.208:1475',
            'https://soar.omega-r.club',
            'https://soar-api.omega-r.club',
        ],
        allow_headers='*',
        supports_credentials=False,
    )

    application.register_blueprint(soar)
    application.register_blueprint(zoom)
    application.register_blueprint(pmt)

    return application


app = create_app()


@app.errorhandler(HTTPException)
def handle_exception(e):
    return jsonify({"message": e.description}), e.code
