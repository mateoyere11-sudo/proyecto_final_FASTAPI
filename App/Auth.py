import os
from datetime import datetime, timedelta, timezone

import bcrypt
import jwt
from jwt import InvalidTokenError
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 30


def hashear_password(password: str) -> str:
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hash_bytes = bcrypt.hashpw(password_bytes, salt)
    return hash_bytes.decode("utf-8")


def verificar_password(password_plano: str, password_hash: str) -> bool:
    return bcrypt.checkpw(password_plano.encode("utf-8"), password_hash.encode("utf-8"))


def crear_token(datos: dict) -> str:
    datos_a_codificar = datos.copy()
    expiracion = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    datos_a_codificar.update({"exp": expiracion})
    token = jwt.encode(datos_a_codificar, SECRET_KEY, algorithm=ALGORITHM)

    return token


def verificar_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except (jwt.ExpiredSignatureError, InvalidTokenError):
        raise ValueError("TOKEN Invalido o expirado")


def obtener_usuario_actual(token: str = Depends(oauth2_scheme)) -> dict:
    try:
        payload = verificar_token(token)
    except ValueError:
        raise HTTPException(
            status_code=401,
            detail="token invalido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload

# python -c "import secrets; print(secrets.token_hex(32))"