import typing as ty
from abc import ABC, abstractmethod

from .dto import ZoomToken


class ZoomAuthIface(ABC):
    """Zoom authentication interface"""

    @abstractmethod
    def get_auth_header(self) -> ty.Dict[str, str]:
        """Get auth header string: Authorization: Bearer <token>"""

    @abstractmethod
    def obtain_token(self):
        """Get token info"""

    @abstractmethod
    def refresh_token(self):
        """Refresh token info"""

    @property
    @abstractmethod
    def expired(self) -> bool:
        """Check if token expired"""


class TokenStorageIface(ABC):
    """Token storage for sharing access between multithread uwsgi context"""

    @abstractmethod
    def save(self, token: ZoomToken):
        """Save token into storage"""

    @abstractmethod
    def get(self) -> ZoomToken:
        """Get token from storage"""
