from datetime import timedelta

from celery import Celery

from app import app
import notification # noqa Need to autodiscover tasks from celery


celery = Celery(app.import_name)
celery.conf.update(app.config)
celery.conf.timezone = 'UTC'
celery.autodiscover_tasks(['notification'])

celery.conf.beat_schedule = {
    'check-data-in-firebase': {
        'task': 'notification.tasks.send_reminders',
        'schedule': timedelta(seconds=60),
    },
}