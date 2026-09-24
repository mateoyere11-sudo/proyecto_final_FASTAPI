from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..Schemas import usuario as schemas
from ..crud import usuario as usuario_crud
from ..database import get_db
from ..Auth import verificar_password, crear_token

router = APIRouter(tags=["Auth"])

@router.post("/register", response_model=schemas.UsuarioResponse, status_code=status.HTTP_201_CREATED)
def register(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    existente = usuario_crud.get_usuario_by_username(db, usuario.username)
    if existente:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    return usuario_crud.create_usuario(db, usuario)

@router.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = usuario_crud.get_usuario_by_username(db, form_data.username)
    if not usuario or not verificar_password(form_data.password, usuario.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = crear_token({"sub": usuario.username})
    return {"access_token": token, "token_type": "bearer"}