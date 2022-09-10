import pytz
import logging
from datetime import datetime

from flask import Blueprint, current_app, abort
from flask_pydantic import validate
from firebase_admin.firestore import firestore

from libs.zoom import CreateMeeting, ZoomError, ZoomAPiClient
from .models import (
    MeetingRequest,
    MeetingResponse,
    MeetingQuery,
    MeetingsResponse,
    MeetingUpdRequest,
    MeetingRetrieveResponse,
)


logger = logging.getLogger(__name__)

zoom = Blueprint('zoom', __name__, url_prefix='/zoom')


@zoom.route('/meeting', methods=['POST'])
@validate()
def create_meeting(body: MeetingRequest):
    """Creates meeting in zoom and save data into firestore"""

    z_cli = current_app.config['ZOOM_API']
    db = current_app.config['FIRESTORE']

    start_time = None
    timezone = None
    if body.start_time:
        dt_utc = body.start_time.astimezone(pytz.UTC)
        start_time = dt_utc.strftime('%Y-%m-%dT%H:%M:%S')
        timezone = 'UTC'

    payload = CreateMeeting(
        agenda=body.agenda,
        topic=body.topic,
        start_time=start_time,
        timezone=timezone,
        duration=body.duration,
    )
    try:
        meeting = z_cli.create_meeting('me', payload)
    except ZoomError as err:
        return {'error': err.message, 'data': err.data}, 400

    item = {
        'created_by': body.created_by,
        'company_id': body.company_id,
        'module_id': body.module_id,
        'created_at': datetime.now(tz=pytz.UTC).isoformat(),
        'meeting': meeting.dict()
    }

    m_ref = db.collection(u'meetings').add(item)
    item['id'] = m_ref[1].id
    return MeetingResponse(**item), 201


@zoom.route('/meeting', methods=['GET'])
@validate()
def get_meetings(query: MeetingQuery):
    """Get meetings from firestore."""

    db = current_app.config['FIRESTORE']
    user_id = query.created_by
    company_id = query.company_id

    m_query = db.collection(u'meetings')
    if user_id:
        m_query = m_query.where(u'created_by', u'==', user_id)
    if company_id:
        m_query = m_query.where(u'company_id', u'==', company_id)

    m_query = m_query.order_by(u'meeting.start_time', direction=firestore.Query.ASCENDING)
    meetings = []
    for row in m_query.stream():
        d = row.to_dict()
        d.update({'id': row.id})
        meetings.append(d)

    return MeetingsResponse(results=meetings)


@zoom.route('/meeting/<meeting_id>', methods=['GET'])
@validate()
def retrieve_meeting(meeting_id: str):
    """Retrieve meeting by its id from firestore"""

    db = current_app.config['FIRESTORE']

    meeting_ref = db.collection(u'meetings').document(meeting_id)
    meeting = meeting_ref.get()
    if not meeting.exists:
        abort(404)
    data = meeting.to_dict()
    print(data)
    return MeetingRetrieveResponse(**data)


@zoom.route('/meeting/<meeting_id>', methods=['PATCH'])
@validate()
def update_meeting(meeting_id: str, body: MeetingUpdRequest):
    """Update meeting"""

    z_cli: ZoomAPiClient = current_app.config['ZOOM_API']
    db = current_app.config['FIRESTORE']

    meeting_ref = db.collection(u'meetings').document(meeting_id)
    meeting = meeting_ref.get()
    if not meeting.exists:
        abort(404)
    else:
        meeting = meeting.to_dict()

    payload = CreateMeeting()
    payload.agenda = body.agenda
    payload.topic = body.topic
    payload.duration = body.duration
    if body.start_time:
        dt_utc = body.start_time.astimezone(pytz.UTC)
        start_time = dt_utc.strftime('%Y-%m-%dT%H:%M:%S')
        timezone = 'UTC'
        payload.start_time = start_time
        payload.timezone = timezone

    try:
        z_cli.update_meeting(id_=meeting['meeting']['id'], payload=payload)
        z_meeting = z_cli.get_meeting(id_=meeting['meeting']['id'])
    except ZoomError as err:
        return {'error': err.message, 'data': err.data}, 409

    meeting['meeting'] = z_meeting.dict()
    meeting['modified_at'] = datetime.now(tz=pytz.UTC).isoformat()
    meeting_ref.set(meeting)

    return MeetingResponse(**meeting)


@zoom.route('/meeting/<meeting_id>', methods=['DELETE'])
@validate()
def delete_meeting(meeting_id: str):
    """Delete meeting from firestore and from zoom"""

    db = current_app.config['FIRESTORE']
    z_cli = current_app.config['ZOOM_API']
    doc = db.collection(u'meetings').document(meeting_id).get()
    if doc.exists:
        data = doc.to_dict()
        meeting_id = data['meeting']['id']
        try:
            z_cli.delete_meeting(meeting_id)
        except ZoomError as err:
            data = err.data
            logger.error(err.message)
            logger.error(data)
        db.collection(u'meetings').document(doc.id).delete()
    return {}, 204

