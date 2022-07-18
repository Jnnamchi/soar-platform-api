from typing import List, Optional, Union
from enum import IntEnum
import datetime
from pydantic import BaseModel


class ZoomToken(BaseModel):
    access_token: str
    token_type: str
    refresh_token: Optional[str]
    expires_in: int
    scope: str


class Meeting(BaseModel):
    agenda: Optional[str]
    created_at: datetime.datetime
    duration: int
    host_id: str
    id: int
    join_url: str
    pmi: Optional[str]
    start_time: datetime.datetime
    timezone: str
    topic: str
    type: int
    uuid: str


class MeetingsList(BaseModel):
    next_page_token: Optional[str]
    page_count: int
    page_number: int
    page_size: int
    total_records: int
    meetings: List[Meeting]


class MType(IntEnum):
    INSTANT = 1
    SCHEDULED = 2
    RECURRING_NO_FIXED = 3
    RECURRING_FIXED = 4


class CreateMeeting(BaseModel):
    agenda: Optional[str]
    default_password: Optional[bool]
    duration: Optional[int]
    password: Optional[str]
    pre_schedule: Optional[bool]
    schedule_for: Optional[str]
    start_time: Optional[str]
    template_id: Optional[str]
    timezone: Optional[str]
    topic: Optional[str]
    type: Optional[MType]

