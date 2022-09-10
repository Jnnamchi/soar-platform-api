import logging
import typing as ty
from enum import Enum
from functools import partial

from pydantic import parse_obj_as
import requests

from .dto import Meeting, MeetingsList, CreateMeeting
from .abs import ZoomAuthIface
from .error import ZoomApiError


logger = logging.getLogger(__name__)


Method = ty.Literal['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']


class MeetingType(Enum):
    LIVE = 'live'
    SCHEDULED = 'scheduled'
    UPCOMING = 'upcoming'
    UPCOMING_MEETINGS = 'upcoming_meetings'
    PREVIOUS_MEETINGS = 'previous_meetings'


class ZoomAPiClient:
    """Zoom's API client."""

    base_url: str = 'https://api.zoom.us'
    api_ver: str = 'v2'

    def __init__(self, auth: ZoomAuthIface):
        self.auth = auth

    def _call(self,
              method: Method,
              path: str,
              data: dict = None,
              auth: bool = True,
              version: ty.Optional[str] = None) -> requests.Response:

        if self.auth.expired:
            self.auth.refresh_token()

        if version is None:
            version = self.api_ver

        call_url = self.base_url.rstrip('/') + f'/{version}/' + path.lstrip('/')

        if method.lower() == 'get':
            req = partial(requests.request, params=data)
        else:
            req = partial(requests.request, json=data)

        headers = {'Accept': 'application/json'}
        if auth:
            headers.update(self.auth.get_auth_header())

        try:
            resp = req(method, call_url, headers=headers)
            if resp.status_code == requests.codes.bad:
                error = resp.json()
                raise ZoomApiError(message='Zoom API Bad request', data=error)
            if resp.status_code == requests.codes.not_found:
                error = resp.json()
                raise ZoomApiError(message='Zoom API Bad request', data=error)

            if resp.status_code == requests.codes.unauthorized:
                error = resp.json()
                raise ZoomApiError(message='Unexpected auth error', data=error)

            # Raise for other HTTPError types
            resp.raise_for_status()
        except ImportError as err:
            logger.error(str(err))
            raise ZoomApiError(str(err))

        return resp

    def get_meetings(self,
                     user: str,
                     m_type: ty.Optional[MeetingType] = None,
                     next_page_token: ty.Optional[str] = None,
                     page_number: ty.Optional[int] = None,
                     page_size: ty.Optional[int] = None) -> MeetingsList:

        """Use this API to list a user's (meeting host) scheduled meetings. For user-level apps, pass the `me` value
        instead of the userId parameter. """

        path = f'users/{user}/meetings'

        data = dict()
        if m_type:
            data['type'] = m_type.value
        if next_page_token:
            data['next_page_token'] = next_page_token
        if page_number:
            data['page_number'] = page_number
        if page_size:
            data['page_size'] = page_size

        resp = self._call('GET', path, data=data)
        try:
            resp_data = resp.json()
        except requests.exceptions.JSONDecodeError as err:
            raise ZoomApiError(f'JSON decode error: {str(err)}')

        return parse_obj_as(MeetingsList, resp_data)

    def create_meeting(self, user: str, payload: CreateMeeting) -> Meeting:
        """Use this API to create a meeting for a user. For user-level apps, pass the `me` value instead of the
        userId parameter. """

        path = f'users/{user}/meetings'

        resp = self._call('POST', path, data=payload.dict())
        try:
            resp_data = resp.json()
        except requests.exceptions.JSONDecodeError as err:
            raise ZoomApiError(f'JSON decode error: {str(err)}')

        return parse_obj_as(Meeting, resp_data)

    def update_meeting(self, id_: int, payload: CreateMeeting):
        """Use this API to update a meeting's details."""

        path = f'meetings/{id_}'
        self._call('PATCH', path, data=payload.dict(exclude_unset=True))

    def get_meeting(self, id_: int) -> Meeting:
        """Retrieve the details of a meeting."""

        path = f'meetings/{id_}'

        resp = self._call('GET', path)
        try:
            resp_data = resp.json()
        except requests.exceptions.JSONDecodeError as err:
            raise ZoomApiError(f'JSON decode error: {str(err)}')

        return parse_obj_as(Meeting, resp_data)

    def delete_meeting(self, meeting_id: str):
        """Delete a meeting."""

        path = f'meetings/{meeting_id}'
        self._call('DELETE', path)
