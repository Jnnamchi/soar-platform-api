import logging
from typing import Optional
from abc import ABC, abstractmethod

from .transport import TransportIface, EmailSMTPTransport
from .dto import EmailTemplate
from .utils import check_email_address


class AgentIface(ABC):

    @abstractmethod
    def send(self, recipients: list[str], template: EmailTemplate):
        """Send email to recipients"""


class EmailAgent(AgentIface):

    transport: TransportIface

    def __init__(self, transport: Optional[TransportIface] = None):
        if transport:
            self.transport = transport
        else:
            self.transport = EmailSMTPTransport.from_config()

    def send(self, recipients: list[str], template: EmailTemplate):

        for addr in recipients:
            if not check_email_address(addr):
                msg = f'Invalid email address {addr}, skipping...'
                logging.error(msg)
                continue

            self.transport.send(addr, template.subj, template.message, template.html)
