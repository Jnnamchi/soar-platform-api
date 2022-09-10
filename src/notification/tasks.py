import logging
import datetime
import pytz
import smtplib
import typing as ty

from celery import shared_task
from app import app

from notification.email.agent import EmailAgent
from notification.email.dto import EmailTemplate
from .tempaltes import TEMPLATES


def find_template(name: str) -> ty.Union[EmailTemplate, None]:
    temps = list(filter(lambda i: i.name.lower() == name.lower(), TEMPLATES))
    if temps:
        return temps.pop()


@shared_task
def send_reminders():
    with app.app_context():
        db = app.config['FIRESTORE']
        agent = EmailAgent()
        now = datetime.datetime.now(tz=pytz.UTC)
        reminders = db.collection('emails').where('date', u'<', now).get()

        for row in reminders:
            data = row.to_dict()
            print('Data: ', data)
            try:
                templ = find_template(data['template'])
                if templ is None:
                    print('Template not found ...')
                    continue
                for email in data['recipients']:
                    agent.send([email], templ)

                db.collection(u'emails').document(row.id).delete()

            except KeyError as err:
                logging.error(f'Invalid document structure: {err}')
                continue
            except smtplib.SMTPDataError as err:
                logging.error(f'Email agent failed: {err}')
                continue
