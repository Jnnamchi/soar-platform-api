import datetime
import pytz

from celery import shared_task
from app import app
from account.repository import TwoFAFireBaseRepository


@shared_task
def clear_old_2fa_sessions():
    with app.app_context():
        db = app.config['FIRESTORE']
        repo = TwoFAFireBaseRepository(session=db)
        now = datetime.datetime.now(tz=pytz.UTC)
        end = now + datetime.timedelta(seconds=300)
        repo.delete_old_sessions(end)

