import re


def wraps_default_html(message: str) -> str:
    html = """
    <html>
      <head></head>
      <body>
        <p>
           {message}
        </p>
      </body>
    </html>
    """
    return html.format(message=message)


def check_email_address(email: str) -> bool:
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return bool(re.fullmatch(pattern, email))
