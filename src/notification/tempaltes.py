from notification.email.dto import EmailTemplate


TEMPLATES: list[EmailTemplate] = [
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