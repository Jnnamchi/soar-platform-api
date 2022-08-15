import time
import base64
import logging
import pickle
import typing as ty
from pathlib import Path
from urllib.parse import urlencode

import requests
import portalocker
from pydantic import parse_obj_as

from .abs import ZoomAuthIface, TokenStorageIface
from .dto import ZoomToken
from .error import ZoomAuthError


logger = logging.getLogger()


class TokenFileStorage(TokenStorageIface):
    """Token storage based on filesystem"""

    def __init__(self, name: str = '__zoom_s2s_oauth.dat', path: Path = Path('.')):
        self.name = name
        self.path = path
        warn = 'Attention! this storage is only thread safe, but not multiple server safe! ' \
               'To serve token data on multi server config, use another storage type '
        logger.warning(warn)

    def save(self, token: ZoomToken):
        name = self.path / self.name
        with portalocker.Lock(name, 'wb', timeout=5) as fh:
            pickle.dump(token, fh)

    def get(self) -> ty.Union[ZoomToken, None]:
        file = self.path / self.name
        if not file.is_file():
            return None
        with portalocker.Lock(file, 'rb', timeout=5) as fh:
            token = pickle.load(fh)
        return token


class ZoomS2SOAuth(ZoomAuthIface):

    MIN_LIFETIME = 3300
    last_obtain: int
    base_url: str = 'https://zoom.us/oauth/token'
    storage: TokenStorageIface

    def __init__(self,
                 client_id: str,
                 client_secret: str,
                 account_id: str,
                 storage: ty.Optional[TokenStorageIface] = None):
        self.account_id = account_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.last_obtain = 0

        if storage:
            self.storage = storage
        else:
            self.storage = TokenFileStorage()

    @property
    def _b64_client_auth_kv(self) -> str:
        string = f'{self.client_id}:{self.client_secret}'
        b64 = base64.b64encode(string.encode('utf-8'))
        return b64.decode('utf-8')

    @property
    def expired(self) -> bool:
        token = self.storage.get()
        if token is None:
            logger.warning('Token is none => expired')
            return True
        current = int(time.time())
        return current >= self.last_obtain + token.expires_in - self.MIN_LIFETIME

    def obtain_token(self):
        url_params = {
            'grant_type': 'account_credentials',
            'account_id': self.account_id,
        }
        url = f'{self.base_url}?{urlencode(url_params)}'
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Basic {self._b64_client_auth_kv}'
        }
        try:
            resp = requests.post(url, headers=headers)
            if resp.status_code == requests.codes.unauthorized:
                error = resp.json()
                raise ZoomAuthError(message='Zoom API Auth error', data=error)
            if resp.status_code == requests.codes.bad:
                error = resp.json()
                raise ZoomAuthError(message='Zoom API Bad request', data=error)

            # Raise for other HTTPError types
            resp.raise_for_status()
            token = parse_obj_as(ZoomToken, resp.json())
            self.storage.save(token=token)
            self.last_obtain = int(time.time())
        except requests.exceptions.RequestException as err:
            logger.error(str(err))
            raise ZoomAuthError(str(err))
        except requests.exceptions.JSONDecodeError as err:
            logger.error(str(err))
            raise ZoomAuthError(str(err))

    def refresh_token(self):
        logger.debug('In token refresh')
        self.obtain_token()

    def get_auth_header(self) -> ty.Dict[str, str]:
        token = self.storage.get()
        if token is None:
            raise ZoomAuthError('Token is not obtained yet.')
        if self.expired:
            raise ZoomAuthError('Token expired, please refresh it.')
        return {'Authorization': f'Bearer {token.access_token}'}