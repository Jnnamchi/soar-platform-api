from flask import current_app
from werkzeug.security import check_password_hash

from account.service import UserGetByEmailRawService


def authenticate(username: str, password: str):
    session = current_app.config['FIRESTORE']
    service = UserGetByEmailRawService(session)
    user = service.invoke(email=username)
    if user and user.is_active and check_password_hash(user.password, password):
        return user

