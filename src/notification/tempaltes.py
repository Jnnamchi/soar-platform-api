import typing as ty
from notification.email.dto import EmailTemplate


TEMPLATES: ty.List[EmailTemplate] = [
    EmailTemplate(
        name='Greeting',
        subj='Greeting!',
        message='Hello! Welcome to Soarline!',
    ),
    EmailTemplate(
        name='Registration Email',
        subj='Registration completed!',
        message='Congratulations! You have registered for the soarline growth module.',
    ),
]