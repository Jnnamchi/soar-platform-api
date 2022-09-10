import datetime
import typing as ty
from pydantic import BaseModel

from libs.zoom import Meeting


class MeetingRequest(BaseModel):
    created_by: str
    company_id: str
    module_id: str
    start_time: ty.Optional[datetime.datetime]
    topic: ty.Optional[str]
    agenda: ty.Optional[str]
    duration: ty.Optional[int]


class MeetingUpdRequest(BaseModel):
    start_time: ty.Optional[datetime.datetime]
    topic: ty.Optional[str]
    agenda: ty.Optional[str]
    duration: ty.Optional[int]


class MeetingResponse(BaseModel):
    id: ty.Optional[str]
    created_by: ty.Optional[str]
    company_id: ty.Optional[str]
    module_id: ty.Optional[str]
    created_at: ty.Optional[str]
    modified_at: ty.Optional[str]
    meeting: Meeting


class MeetingRetrieveResponse(BaseModel):
    created_by: ty.Optional[str]
    company_id: ty.Optional[str]
    module_id: ty.Optional[str]
    created_at: ty.Optional[str]
    modified_at: ty.Optional[str]
    meeting: Meeting


class MeetingQuery(BaseModel):
    created_by: ty.Optional[str]
    company_id: ty.Optional[str]


class MeetingsResponse(BaseModel):
    results: ty.List[MeetingResponse]
