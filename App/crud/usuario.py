from sqlalchemy.orm import Session
from ..models.usuarios import Usuario
from ..Schemas import usuario as schemas
from ..Auth import hashear_password

def get_usuario_by_username(db: Session, username: str):
    return db.query(Usuario).filter(Usuario.username == username).first()

def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    nuevo_usuario = Usuario(
        username=usuario.username,
        email=usuario.email,
        password_hash=hashear_password(usuario.password)
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario