import logging

from flask import Blueprint, current_app, abort, Response
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import create_access_token
from flask_pydantic import validate

from .auth import authenticate
from .service import (
    ServiceError,
    UserGetByIdService,
    UserCreateService,
    UsersListService,
    UserUpdateService,
    UserDeleteService,
    UserSignupStartService,
    UserSignupCompleteService,
    GetSignupService,
    TFAInitService,
    FinishTFAService,
    InviteStartService,
    InviteFinishService,
    ResetPasswordStartService,
    ResetPasswordFinishService,
)

from . import schemas


logger = logging.getLogger(__name__)

account = Blueprint('account', __name__, url_prefix='/account')


@account.route('/auth', methods=['POST'])
@validate()
def get_token(body: schemas.UserLogin):
    """Simple login"""

    user = authenticate(body.email, body.password)
    if user:
        access_token = create_access_token(identity=user.id)
        return schemas.TokenResponse(access_token=access_token)
    else:
        abort(401, "Invalid credentials")


@account.route('/2fa', methods=['POST'])
@validate()
def init_2fa(body: schemas.UserLogin):
    """Init 2fa session"""

    session = current_app.config['FIRESTORE']
    service = TFAInitService(session)
    user = authenticate(body.email, body.password)
    if user:
        return service.invoke(user)
    else:
        abort(401, "Invalid credentials")


@account.route('/2fa/<tfa_id>', methods=['POST'])
@validate()
def finish_2fa(tfa_id: str, body: schemas.TFACodeRequest):
    """Finish 2fa session and get token"""

    session = current_app.config['FIRESTORE']
    service = FinishTFAService(session)
    user_id = service.invoke(tfa_id, body.code)
    if user_id:
        access_token = create_access_token(identity=user_id)
        return schemas.TokenResponse(access_token=access_token)
    else:
        abort(401, "Invalid Code")


@account.route('/participant/invite', methods=['POST'])
@validate()
@jwt_required()
def invite_participant(body: schemas.InviteUserRequest):
    """Invite user to company"""

    user_id = get_jwt_identity()
    session = current_app.config['FIRESTORE']
    service = InviteStartService(session)
    service.invoke(user_id, body.email)
    return Response(status=204)


@account.route('/participant/accept', methods=['POST'])
@validate()
def accept_invitation(body: schemas.AcceptInvitation):
    """Participant accept invitation"""

    session = current_app.config['FIRESTORE']
    service = InviteFinishService(session)
    service.invoke(body)
    return Response(status=204)


@account.route('/user', methods=['GET'])
@validate()
@jwt_required()
def get_users():
    """Get users list"""

    session = current_app.config['FIRESTORE']
    service = UsersListService(session)
    try:
        return service.invoke()
    except Exception as e:
        abort(404, str(e))


@account.route('/user/<user_id>', methods=['GET'])
@validate()
@jwt_required()
def retrieve_user(user_id: str):
    """Retrieve user by its id from firestore"""

    session = current_app.config['FIRESTORE']
    service = UserGetByIdService(session)
    try:
        user = service.invoke(user_id)
        if user is None:
            abort(404, f'User {user_id} does not exists.')
        return schemas.UserResponse(**user.dict())
    except Exception as e:
        abort(404, str(e))


@account.route('/me', methods=['GET'])
@validate()
@jwt_required()
def get_yourself():
    """Get yourself"""

    user_id = get_jwt_identity()
    session = current_app.config['FIRESTORE']
    service = UserGetByIdService(session)
    try:
        user = service.invoke(user_id)
        if user is None:
            abort(404, f'User {user_id} does not exists.')
        return schemas.UserResponse(**user.dict())
    except Exception as e:
        abort(404, str(e))


@account.route('/user', methods=['POST'])
@validate()
@jwt_required()
def create_user(body: schemas.UserInput):
    """Create User"""
    
    session = current_app.config['FIRESTORE']
    service = UserCreateService(session)
    try:
        user = service.invoke(body)
        return schemas.UserResponse(**user.dict())
    except Exception as e:
        abort(404, str(e))


@account.route('/user/<user_id>', methods=['PUT'])
@validate()
@jwt_required()
def update_user(user_id: str, body: schemas.UserInput):
    """Update user"""

    session = current_app.config['FIRESTORE']
    service = UserUpdateService(session)
    try:
        user = service.invoke(user_id, body)
        return schemas.UserResponse(**user.dict())
    except Exception as e:
        abort(404, str(e))


@account.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id: str):
    """Update user"""

    session = current_app.config['FIRESTORE']
    service = UserDeleteService(session)
    try:
        service.invoke(user_id)
        return Response(status=204)
    except Exception as e:
        abort(404, str(e))


@account.route('/signup', methods=['POST'])
@validate()
def admin_signup_begin(body: schemas.SignupStart):
    """Signup begin"""

    session = current_app.config['FIRESTORE']
    service = UserSignupStartService(session)
    service.invoke(body)
    return Response(status=204)


@account.route('/signup/<request_id>', methods=['POST'])
def admin_signup_complete(request_id: str):
    """Signup complete"""

    session = current_app.config['FIRESTORE']
    service = UserSignupCompleteService(session)
    service.invoke(request_id)
    return Response(status=204)


@account.route('/signup/<request_id>', methods=['GET'])
@validate()
def retrieve_signup_request(request_id: str):
    session = current_app.config['FIRESTORE']
    service = GetSignupService(session)
    item = service.invoke(request_id)
    if not item:
        abort(404, 'Signup request does not exists.')
    return item


@account.route('/reset-password', methods=['POST'])
@validate()
def reset_password_start(body: schemas.ResetPasswordStart):
    session = current_app.config['FIRESTORE']
    service = ResetPasswordStartService(session)
    service.invoke(email=body.email)
    return Response(status=204)


@account.route('/reset-password/<request_id>', methods=['POST'])
@validate()
def reset_password_finish(request_id: str, body: schemas.ResetPasswordFinish):
    session = current_app.config['FIRESTORE']
    service = ResetPasswordFinishService(session)
    service.invoke(request_id=request_id, password=body.password)
    return Response(status=204)

