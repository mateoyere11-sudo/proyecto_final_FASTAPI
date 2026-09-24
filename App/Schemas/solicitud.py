from datetime import date

from pydantic import BaseModel, ConfigDict


class SolicitudBase(BaseModel):
    cliente: str
    fecha: date
    servicio_id: int


class SolicitudCreate(SolicitudBase):
    pass


class SolicitudResponse(SolicitudBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class SolicitudUpdate(BaseModel):
    cliente: str | None = None
    fecha: date | None = None
    servicio_id: int | None = None