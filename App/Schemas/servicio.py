from pydantic import BaseModel, ConfigDict


class ServicioBase(BaseModel):
    nombre: str
    precio: int


class ServicioCreate(ServicioBase):
    pass


class ServicioResponse(ServicioBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class ServUpdate(BaseModel):
    nombre: str | None = None
    precio: int | None = None


ServicioUpdate = ServUpdate