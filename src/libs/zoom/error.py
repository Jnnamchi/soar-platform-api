import typing as ty
import logging
import contextlib
from http.client import HTTPConnection


class ZoomError(Exception):
    """Base exception"""

    def __init__(self, message: str, data: ty.Optional[dict] = None):
        self.message = message
        self.data = data

    def __str__(self):
        return self.message


class ZoomAuthError(ZoomError):
    """Zoom auth error"""


class ZoomApiError(ZoomError):
    """Zoom API error"""


def debug_requests_on():
    """Switches on logging of the requests' module."""
    HTTPConnection.debuglevel = 1

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


def debug_requests_off():
    """Switches off logging of the requests' module, might be some side effects"""
    HTTPConnection.debuglevel = 0

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.WARNING)
    root_logger.handlers = []
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.WARNING)
    requests_log.propagate = False


@contextlib.contextmanager
def debug_requests():
    """Use with 'with'!"""
    debug_requests_on()
    yield
    debug_requests_off()
