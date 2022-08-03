from typing import Optional
from abc import ABC, abstractmethod

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate, make_msgid

from .utils import wraps_default_html
from .config import SmtpConfig


class TransportIface(ABC):

    @abstractmethod
    def send(self, to: str, subj: str, message: str, html: Optional[str] = None):
        """Send email to recipient"""


class EmailSMTPTransport(TransportIface):

    def __init__(self,
                 from_: str,
                 host: str,
                 port: int,
                 user: str,
                 passw: str,
                 use_auth: Optional[bool] = True,
                 tsl: Optional[bool] = True):
        self.from_ = from_
        self.host = host
        self.port = port
        self.user = user
        self.passw = passw
        self.use_auth = use_auth
        self.tsl = tsl

    def send(self, to: str | list[str], subj: str, message: str, html: Optional[str] = None):
        """Send email."""

        if isinstance(to, list):
            rec = ', '.join(to)
        else:
            rec = to

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subj
        msg['From'] = self.from_
        msg['To'] = rec
        msg['Date'] = formatdate(localtime=True)
        msg['Message-Id'] = make_msgid()

        if html is None:
            html = wraps_default_html(message)

        part1 = MIMEText(message, 'plain')
        part2 = MIMEText(html, 'html')

        msg.attach(part1)
        msg.attach(part2)

        mail = smtplib.SMTP(self.host, self.port)

        mail.ehlo()

        if self.tsl:
            mail.starttls()

        if self.use_auth:
            mail.login(self.user, self.passw)

        mail.sendmail(self.from_, to, msg.as_string())
        mail.quit()

    @classmethod
    def from_config(cls, config: Optional[SmtpConfig] = None) -> 'EmailSMTPTransport':
        if config is None:
            config = SmtpConfig()

        return cls(
            config.sender,
            config.host,
            config.port,
            config.user,
            config.passw,
            config.use_auth,
            config.tsl,
        )
