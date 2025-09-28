from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from app.core.config import settings

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def create_access_token(subject: str | int, expires_delta: int | None = None):
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES if expires_delta is None else expires_delta)
    to_encode = {'exp': expire, 'sub': str(subject)}
    encoded = jwt.encode(to_encode, settings.SECRET_KEY, algorithm='HS256')
    return encoded

def decode_access_token(token: str):
    return jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
