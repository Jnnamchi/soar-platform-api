import os
import logging

from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
from flask_cors import CORS

from soar.routes import soar
from zoom.views import zoom
from payment.views import pmt
from prestart import init_stripe, init_firestore, init_zoom_api

from flask_cors import CORS, cross_origin

def create_app() -> Flask:
    application = Flask(__name__)

    application.config.update(CELERY_BROKER_URL=os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0'))
    application.config.update(result_backend=os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0'))

    with application.app_context():
        try:
            init_firestore(application)
            init_zoom_api(application)
            init_stripe(application)
        except Exception as e:
            logging.error(e)
            quit(1)

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

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.errorhandler(HTTPException)
def handle_exception(e):
    return jsonify({"message": e.description}), e.code
