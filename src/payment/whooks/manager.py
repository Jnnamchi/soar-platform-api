from abc import ABC, abstractmethod

from stripe import Event


class HookHandlerIface(ABC):

    @abstractmethod
    def handle(self):
        pass


class WHookError(Exception):
    """Base Stripe hooks exception"""


class BaseHookHandler(HookHandlerIface):

    def __init__(self, event: Event):
        self.event = event

    def handle(self):
        raise NotImplementedError


class PmtSuccessHandler(BaseHookHandler):

    def handle(self):
        print(self.event)


class PmtFailedHandler(BaseHookHandler):

    def handle(self):
        print(self.event)


class PmtCreatedHandler(BaseHookHandler):

    def handle(self):
        print(self.event)


class SessionCompleteHandler(BaseHookHandler):

    def handle(self):
        print(self.event)


class WHookManager:

    handler: HookHandlerIface

    def __init__(self, handler: HookHandlerIface):
        self.handler = handler

    @classmethod
    def create(cls, event: Event) -> 'WHookManager':
        mapper = {
            'payment_intent.created': PmtCreatedHandler,
            'payment_intent.succeeded': PmtSuccessHandler,
            'payment_intent.payment_failed': PmtFailedHandler,
            'checkout.session.completed': SessionCompleteHandler,
        }

        try:
            handler_class = mapper[event.type]
            handler = handler_class(event)
        except KeyError:
            raise WHookError(f'Handler for type {event.type} not implemented.')

        return cls(handler)

    def handle(self):
        self.handler.handle()
