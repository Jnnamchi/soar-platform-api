import typing as ty

from pydantic import BaseModel


_RM = ty.TypeVar('_RM', bound=BaseModel) # noqa read model
_WM = ty.TypeVar('_WM', bound=BaseModel) # noqa write model


class RepositoryProtocol(ty.Protocol[_RM, _WM]):

    def get_by_id(self, _id: ty.Any) -> _RM:
        ...

    def get_all(self) -> list[_RM]:
        ...

    def create(self, item: _WM) -> _RM:
        ...

    def update(self, _id: ty.Any, item: _WM) -> _RM:
        ...

    def delete(self, _id: ty.Any):
        ...


class SignupProtocol(ty.Protocol[_RM, _WM]):

    def get_by_id(self, _id: ty.Any) -> _RM:
        ...

    def create(self, item: _WM) -> _RM:
        ...

    def delete(self, _id: ty.Any):
        ...


