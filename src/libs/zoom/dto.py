import typing as ty
from enum import IntEnum
import datetime
from pydantic import BaseModel


class ZoomToken(BaseModel):
    access_token: str
    token_type: str
    refresh_token: ty.Optional[str]
    expires_in: int
    scope: str


class Meeting(BaseModel):
    agenda: ty.Optional[str]
    created_at: datetime.datetime
    duration: int
    host_id: str
    id: int
    join_url: str
    pmi: ty.Optional[str]
    start_time: datetime.datetime
    timezone: str
    topic: str
    type: int
    uuid: str


class MeetingsList(BaseModel):
    next_page_token: ty.Optional[str]
    page_count: int
    page_number: int
    page_size: int
    total_records: int
    meetings: ty.List[Meeting]


class MType(IntEnum):
    INSTANT = 1
    SCHEDULED = 2
    RECURRING_NO_FIXED = 3
    RECURRING_FIXED = 4


class CreateMeeting(BaseModel):
    agenda: ty.Optional[str]
    default_password: ty.Optional[bool]
    duration: ty.Optional[int]
    password: ty.Optional[str]
    pre_schedule: ty.Optional[bool]
    schedule_for: ty.Optional[str]
    start_time: ty.Optional[str]
    template_id: ty.Optional[str]
    timezone: ty.Optional[str]
    topic: ty.Optional[str]
    type: ty.Optional[MType]

