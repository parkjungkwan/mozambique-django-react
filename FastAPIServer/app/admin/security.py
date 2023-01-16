import secrets
import string
from typing import Union, Any
from datetime import datetime, timedelta
import shortuuid
from app.admin.utils import utc_seoul

def myuuid():
    alphabet = string.ascii_lowercase + string.digits
    su = shortuuid.ShortUUID(alphabet=alphabet)
    return su.random(length=8)

def get_hashed_password(plain_password: str) -> str:
    pass

def verify_password(plain_password: str, hashed_password: str):
    pass

def generate_token(subject: Union[str, Any], expires_delta: int = None):
    pass

def generate_token_by_secrets():
    return secrets.token_urlsafe(32) # python3.8 기준으로 DEFAULT_ENTROPY == 32

def refresh_token(subject: Union[str, Any], expires_delta: int = None):
    pass

def get_expiration_date():
    return utc_seoul() + timedelta(days=3)
