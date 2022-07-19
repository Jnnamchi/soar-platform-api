import datetime
from typing import List, Optional, Union
from pydantic import BaseModel

from libs.zoom import Meeting


class MeetingRequest(BaseModel):
    created_by: str
    company_id: str
    module_id: str
    start_time: Optional[datetime.datetime]
    topic: Optional[str]
    agenda: Optional[str]
    duration: Optional[int]


class MeetingUpdRequest(BaseModel):
    start_time: Optional[datetime.datetime]
    topic: Optional[str]
    agenda: Optional[str]
    duration: Optional[int]


class MeetingResponse(BaseModel):
    id: Optional[str]
    created_by: Optional[str]
    company_id: Optional[str]
    module_id: Optional[str]
    created_at: Optional[str]
    modified_at: Optional[str]
    meeting: Meeting


class MeetingRetrieveResponse(BaseModel):
    created_by: Optional[str]
    company_id: Optional[str]
    module_id: Optional[str]
    created_at: Optional[str]
    modified_at: Optional[str]
    meeting: Meeting


class MeetingQuery(BaseModel):
    created_by: Optional[str]
    company_id: Optional[str]


class MeetingsResponse(BaseModel):
    results: List[MeetingResponse]
