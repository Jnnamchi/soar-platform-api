import typing as ty


class ServiceProtocol(ty.Protocol):

    def invoke(self, *args, **kwargs) -> ty.Any:
        ...
