from pydantic import BaseModel, EmailStr

class UsuarioCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UsuarioResponse(BaseModel):
    id_usuario: int
    username: str
    email: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class LoginRequest(BaseModel):
    username: str
    password: str