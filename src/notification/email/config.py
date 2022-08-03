from pydantic import BaseSettings


class SmtpConfig(BaseSettings):

    host: str
    port: int = 587
    user: str
    passw: str
    tsl: bool = True
    sender: str
    use_auth: bool = True

    class Config:
        env_prefix = 'SMTP_'
        case_sensitive = False
