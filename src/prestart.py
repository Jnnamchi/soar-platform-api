import os
from pathlib import Path

import stripe
from flask import Flask
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from libs.zoom import ZoomAPiClient, ZoomS2SOAuth


def init_firestore(app: Flask):
    cred_path = Path() / 'credentials.json'
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)
    app.config['FIRESTORE'] = firestore.client()


def init_zoom_api(app: Flask):
    account_id = os.getenv('ZOOM_ACCOUNT_ID', None)
    client_id = os.getenv('ZOOM_CLIENT_ID', None)
    secret = os.getenv('ZOOM_CLIENT_SECRET', None)

    if not all([account_id, client_id, secret]):
        raise Exception('Zoom credentials not found in ENV variables')

    auth = ZoomS2SOAuth(client_id, secret, account_id)
    app.config['ZOOM_API'] = ZoomAPiClient(auth)


def init_stripe(app: Flask):
    key = os.getenv('STRIPE_API_KEY', None)
    whook_secret = os.getenv('STRIPE_WHOOK_SECRET', None)

    if not all([key, whook_secret]):
        raise Exception('STRIPE_API_KEY or STRIPE_WHOOK_SECRET not found in ENV variables')

    stripe.api_key = key
    app.config['STRIPE'] = stripe
    app.config['STRIPE_WHOOK_SECRET'] = whook_secret
