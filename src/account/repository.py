import datetime
import typing as ty

from account.models import (
    UserOut,
    UserIn,
    SignupRequestOut,
    SignupRequestIn,
    TwoFARequestOut,
    TwoFARequestIn,
    UserInvitationIn,
    UserInvitationOut,
    ResetPasswordReqIn,
    ResetPasswordReqOut,
)
from libs.repository import errors
from libs.repository.abstract import RepositoryProtocol


class UserRepositoryProtocol(RepositoryProtocol[UserOut, UserIn], ty.Protocol):

    def get_by_email(self, email: str) -> UserOut:
        ...


class TFARepositoryProtocol(RepositoryProtocol[TwoFARequestOut, TwoFARequestIn], ty.Protocol):

    def get_by_user_id(self, user_id: str) -> TwoFARequestOut:
        ...

    def delete_old_sessions(self, end: datetime.datetime):
        ...


class UserFireBaseRepository:

    def __init__(self, session, collection: str = u'users'):
        self._session = session
        self.collection = collection

    @property
    def session(self):
        return self._session

    def get_by_id(self, _id: ty.Any) -> ty.Union[UserOut, None]:
        ref = self.session.collection(self.collection).document(_id)
        user = ref.get()
        if not user.exists:
            return None

        data = user.to_dict()
        data.update({'id': _id})
        return UserOut(**data)

    def get_by_email(self, email: str) -> ty.Union[UserOut, None]:
        docs = self.session.collection(self.collection).where(u'email', u'==', email.lower()).stream()

        result = None
        for doc in docs:
            data = doc.to_dict()
            data.update({'id': doc.id})
            result = UserOut(**data)
            break

        return result

    def get_all(self) -> list[UserOut]:
        docs = self.session.collection(self.collection).stream()
        results: list[UserOut] = list()
        for doc in docs:
            data = doc.to_dict()
            data.update({'id': doc.id})
            results.append(UserOut(**data))
        return results

    def create(self, item: UserIn) -> UserOut:

        user = self.get_by_email(item.email)
        if user is not None:
            msg = f'User with email {item.email} already exists'
            raise errors.AlreadyExists(msg)

        resp = self.session.collection(self.collection).add(item.dict())
        doc_id = resp[1].id
        data = item.dict()
        data.update({'id': doc_id})
        return UserOut(**data)

    def update(self, _id: ty.Any, item: UserIn) -> UserOut:
        ref = self.session.collection(self.collection).document(_id)

        user = ref.get()
        if not user.exists:
            msg = f'User {_id} does not exists'
            raise errors.DoesNotExists(msg)

        user = user.to_dict()
        if user['email'].lower() != item.email.lower():
            new_email_user = self.get_by_email(item.email)
            if new_email_user is not None:
                msg = f'User with email {item.email} already exists'
                raise errors.AlreadyExists(msg)

        ref.set(item.dict())

        data = item.dict()
        data.update({'id': _id})
        return UserOut(**data)

    def delete(self, _id: ty.Any):
        ref = self.session.collection(self.collection).document(_id)
        user = ref.get()
        if not user.exists:
            msg = f'User {_id} does not exists'
            raise errors.DoesNotExists(msg)

        ref.delete()


class SignupFireBaseRepository:

    def __init__(self, session, collection: str = u'signuprequests'):
        self._session = session
        self.collection = collection

    def get_by_id(self, _id: ty.Any) -> ty.Union[SignupRequestOut, None]:
        ref = self.session.collection(self.collection).document(_id)
        obj = ref.get()
        if not obj.exists:
            return None

        data = obj.to_dict()
        data.update({'id': _id})
        return SignupRequestOut(**data)

    def create(self, item: SignupRequestIn) -> SignupRequestOut:

        resp = self.session.collection(self.collection).add(item.dict())
        doc_id = resp[1].id
        data = item.dict()
        data.update({'id': doc_id})
        return SignupRequestOut(**data)

    def delete(self, _id: ty.Any):
        ref = self.session.collection(self.collection).document(_id)
        obj = ref.get()
        if obj.exists:
            ref.delete()

    @property
    def session(self):
        return self._session


class TwoFAFireBaseRepository:

    def __init__(self, session, collection: str = u'twofarequests'):
        self._session = session
        self.collection = collection

    def get_by_id(self, _id: ty.Any) -> ty.Union[TwoFARequestOut, None]:
        ref = self.session.collection(self.collection).document(_id)
        obj = ref.get()
        if not obj.exists:
            return None

        data = obj.to_dict()
        data.update({'id': _id})
        return TwoFARequestOut(**data)

    def get_by_user_id(self, user_id: str) -> ty.Union[TwoFARequestOut, None]:
        docs = self.session.collection(self.collection).where(u'user_id', u'==', user_id).stream()

        result = None
        for doc in docs:
            data = doc.to_dict()
            data.update({'id': doc.id})
            result = TwoFARequestOut(**data)
            break

        return result

    def create(self, item: TwoFARequestIn) -> TwoFARequestOut:

        resp = self.session.collection(self.collection).add(item.dict())
        doc_id = resp[1].id
        data = item.dict()
        data.update({'id': doc_id})
        return TwoFARequestOut(**data)

    def delete(self, _id: ty.Any):
        ref = self.session.collection(self.collection).document(_id)
        obj = ref.get()
        if obj.exists:
            ref.delete()

    def delete_old_sessions(self, end: datetime.datetime):
        docs = self.session.collection(self.collection).where('created_at', u'>', end).get()
        for row in docs:
            self.session.collection(self.collection).document(row.id).delete()

    @property
    def session(self):
        return self._session


class InvitationFireBaseRepository:

    def __init__(self, session, collection: str = u'invitationrequests'):
        self._session = session
        self.collection = collection

    def get_by_id(self, _id: ty.Any) -> ty.Union[UserInvitationOut, None]:
        ref = self.session.collection(self.collection).document(_id)
        obj = ref.get()
        if not obj.exists:
            return None

        data = obj.to_dict()
        data.update({'id': _id})
        return UserInvitationOut(**data)

    def create(self, item: UserInvitationIn) -> UserInvitationOut:

        resp = self.session.collection(self.collection).add(item.dict())
        doc_id = resp[1].id
        data = item.dict()
        data.update({'id': doc_id})
        return UserInvitationOut(**data)

    def delete(self, _id: ty.Any):
        ref = self.session.collection(self.collection).document(_id)
        obj = ref.get()
        if obj.exists:
            ref.delete()

    @property
    def session(self):
        return self._session


class ResetPasswordFirebaseRepository:

    def __init__(self, session, collection: str = u'resetpasswordrequests'):
        self._session = session
        self.collection = collection

    def get_by_id(self, _id: ty.Any) -> ty.Union[ResetPasswordReqOut, None]:
        ref = self.session.collection(self.collection).document(_id)
        obj = ref.get()
        if not obj.exists:
            return None

        data = obj.to_dict()
        data.update({'id': _id})
        return ResetPasswordReqOut(**data)

    def create(self, item: ResetPasswordReqIn) -> ResetPasswordReqOut:

        resp = self.session.collection(self.collection).add(item.dict())
        doc_id = resp[1].id
        data = item.dict()
        data.update({'id': doc_id})
        return ResetPasswordReqOut(**data)

    def delete(self, _id: ty.Any):
        ref = self.session.collection(self.collection).document(_id)
        obj = ref.get()
        if obj.exists:
            ref.delete()

    @property
    def session(self):
        return self._session

