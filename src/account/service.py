import typing as ty
import random

from flask import abort
from datetime import datetime
import pytz

from account.models import (
    UserOut,
    UserIn,
    SignupRequestOut,
    SignupRequestIn,
    TwoFARequestIn,
    TwoFARequestOut,
    UserInvitationIn,
    UserInvitationOut,
    ResetPasswordReqIn,
    ResetPasswordReqOut,
)
from account.repository import (
    UserFireBaseRepository,
    UserRepositoryProtocol,
    SignupFireBaseRepository,
    TwoFAFireBaseRepository,
    InvitationFireBaseRepository,
    ResetPasswordFirebaseRepository,
)
from account.schemas import (
    UserResponse,
    SignupStart,
    TFASessionResponse,
    AcceptInvitation,
    ResetPasswordStart,
    ResetPasswordFinish,
)

from notification.email.agent import EmailAgent
from notification.email.dto import EmailTemplate

from soar.firebase.companies import addUserCompany, getUserCompanies, addParticipantsToCompany


class ServiceError(Exception):
    """Base service error"""


class _UserBaseService:
    repository: UserRepositoryProtocol

    def __init__(self, session):
        self.repository = UserFireBaseRepository(session=session)


class _BaseSignupService:

    def __init__(self, session):
        self.user_repo = UserFireBaseRepository(session=session)
        self.sup_repo = SignupFireBaseRepository(session=session)


class _Base2FAService:

    def __init__(self, session):
        self.user_repo = UserFireBaseRepository(session=session)
        self.tfa_repo = TwoFAFireBaseRepository(session=session)


class _BaseParticipantService:

    def __init__(self, session):
        self.user_repo = UserFireBaseRepository(session=session)
        self.ptsp_repo = InvitationFireBaseRepository(session=session)


class _BaseResetPasswordService:

    def __init__(self, session):
        self.user_repo = UserFireBaseRepository(session=session)
        self.reset_password_repo = ResetPasswordFirebaseRepository(session=session)


class UserGetByIdService(_UserBaseService):

    def invoke(self, _id: ty.Any) -> UserResponse:

        user = self.repository.get_by_id(_id)
        if user is not None:
            return UserResponse(**self.repository.get_by_id(_id).dict())


class UserGetByIdRawService(_UserBaseService):

    def invoke(self, _id: ty.Any) -> UserOut:

        user = self.repository.get_by_id(_id)
        if user is not None:
            return self.repository.get_by_id(_id)


class UserGetByEmailRawService(_UserBaseService):

    def invoke(self, email: str) -> UserOut:

        return self.repository.get_by_email(email)


class UsersListService(_UserBaseService):

    def invoke(self) -> list[dict]:
        users = self.repository.get_all()
        return [UserResponse(**u.dict()).dict() for u in users]


class UserCreateService(_UserBaseService):

    def invoke(self, item: UserIn) -> UserResponse:
        return UserResponse(**self.repository.create(item).dict())


class UserUpdateService(_UserBaseService):

    def invoke(self, _id: ty.Any, item: UserIn) -> UserResponse:
        return UserResponse(**self.repository.update(_id, item).dict())


class UserDeleteService(_UserBaseService):

    def invoke(self, _id: ty.Any):
        self.repository.delete(_id)


class GetSignupService(_BaseSignupService):

    def invoke(self, _id: str) -> SignupRequestOut:
        req = self.sup_repo.get_by_id(_id)
        if req:
            return SignupRequestOut(**req.dict())
        else:
            abort(404, 'Request does not exists.')


class UserSignupStartService(_BaseSignupService):

    def invoke(self, item: SignupStart):

        user = self.user_repo.get_by_email(item.email)
        if user:
            abort(400, f'Email {item.email} already taken.')

        user_in = UserIn(**item.dict())
        user_in.hash_password()
        created_user = self.user_repo.create(user_in)

        now = datetime.now(tz=pytz.UTC)
        obj = SignupRequestIn(email=item.email, created_at=now)
        created = self.sup_repo.create(obj)

        templ = EmailTemplate(
            name='Signup',
            subj='Complete your registration!',
            message=f'Click https://soar.omega-r.club/registration/complete/{created.id} to activate your user.',
        )
        agent = EmailAgent()
        agent.send([item.email], templ)

        company = dict(
            uuid='',
            name=item.company_name,
            admins=[created_user.id],
            participants=[],
            modules=[],
            size=item.organization_size,
            topAnswers=[],
            category=item.industry,
            virtualWorkshops={},
            inPersonWorkshops={},
            moduleAnswers={},
            answerAnalysis={},
            description=item.job_title,

        )
        addUserCompany(self.user_repo.session, company)


class UserSignupCompleteService(_BaseSignupService):

    def invoke(self, _id: str) -> UserResponse:

        req = self.sup_repo.get_by_id(_id)
        if req:

            user = self.user_repo.get_by_email(req.email)
            if user and user.is_active:
                abort(400, f'Email {req.email} already taken.')

            user.is_active = True
            user_upd = UserIn(**user.dict())
            saved = self.user_repo.update(user.id, user_upd)
            self.sup_repo.delete(_id)
            return UserResponse(**saved.dict())
        else:
            abort(404, f'Request {_id} does not exists.')


class TFAInitService(_Base2FAService):

    def _create_new_tfa(self, user_id: str) -> TwoFARequestOut:
        code = str(random.randint(0, 9999)).rjust(4, '0')
        now = datetime.now(tz=pytz.UTC)
        tfa = TwoFARequestIn(
            user_id=user_id,
            code=code,
            created_at=now,
        )
        return self.tfa_repo.create(tfa)

    def invoke(self, user: UserOut) -> TFASessionResponse:

        tfa = self.tfa_repo.get_by_user_id(user_id=user.id)
        if tfa is None:
            tfa = self._create_new_tfa(user_id=user.id)

        templ = EmailTemplate(
            name='Confirm',
            subj='Confirm sign in!',
            message=f'Code: {tfa.code}',
        )
        agent = EmailAgent()
        agent.send([user.email], templ)
        return TFASessionResponse(**tfa.dict())


class FinishTFAService(_Base2FAService):

    def invoke(self, _id: str, code: str) -> ty.Optional[str]:
        tfa = self.tfa_repo.get_by_id(_id)
        user_id = None
        if tfa:
            if tfa.code == code:
                user_id = tfa.user_id
        self.tfa_repo.delete(_id)
        return user_id


class InviteStartService(_BaseParticipantService):

    def invoke(self, user_id: str, email: str):
        item = UserInvitationIn(
            admin_id=user_id,
            email=email,
            created_at=datetime.now(tz=pytz.UTC),
        )
        created = self.ptsp_repo.create(item)

        templ = EmailTemplate(
            name='Participant signup',
            subj='Complete your registration!',
            message=f'Click https://soar.omega-r.club/registration/complete/participant/{created.id} to finish.',
        )
        agent = EmailAgent()
        agent.send([email], templ)


class InviteFinishService(_BaseParticipantService):

    def invoke(self, item: AcceptInvitation):
        session = self.user_repo.session
        inv = self.ptsp_repo.get_by_id(item.invitation_id)

        user_in = UserIn(
            email=inv.email,
            first_name=item.first_name,
            last_name=item.last_name,
            job_title='',
            phone='',
            is_active=True,
            role='participant',
            password=item.password,
        )
        user_in.hash_password()

        participant = self.user_repo.create(user_in)

        admin = self.user_repo.get_by_id(inv.admin_id)
        companies = getUserCompanies(session, admin.id)
        if companies:
            company = companies[0]
            addParticipantsToCompany(session, company['uuid'], [participant.id])


class ResetPasswordStartService(_BaseResetPasswordService):

    def invoke(self, email: str):
        user = self.user_repo.get_by_email(email)
        if user:
            model = ResetPasswordReqIn(
                email=email,
                created_at=datetime.now(tz=pytz.UTC),
            )
            created = self.reset_password_repo.create(model)

            templ = EmailTemplate(
                name='Resetpassword',
                subj='Password reset message!',
                message=f'Click https://soar.omega-r.club/reset-password/{created.id} to finish.',
            )
            agent = EmailAgent()
            agent.send([email], templ)


class ResetPasswordFinishService(_BaseResetPasswordService):

    def invoke(self, request_id: str, password: str):
        req = self.reset_password_repo.get_by_id(request_id)
        if not req:
            raise ServiceError('Request not found')

        user = self.user_repo.get_by_email(req.email)
        if not user:
            raise ServiceError('User not found.')

        user.password = password
        user_in = UserIn(**user.dict())
        user_in.hash_password()

        self.user_repo.update(user.id, user_in)

        templ = EmailTemplate(
            name='Resetpassword_done',
            subj='Password changed!',
            message=f'Password changed!',
        )
        agent = EmailAgent()
        agent.send([user.email], templ)
