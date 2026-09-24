from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..Schemas import solicitud as schemas
from ..crud import solicitud_servicio as solicitud_crud
from ..database import get_db
from ..Auth import obtener_usuario_actual  

router = APIRouter(prefix="/solicitudes", tags=["Solicitudes"])

@router.get("/", response_model=list[schemas.SolicitudResponse])
def list_solicitudes(db: Session = Depends(get_db), usuario_actual: dict = Depends(obtener_usuario_actual)):
    return solicitud_crud.get_solicitudes(db)

@router.get("/{id_solicitud}", response_model=schemas.SolicitudResponse)
def get_solicitud(id_solicitud: int, db: Session = Depends(get_db), usuario_actual: dict = Depends(obtener_usuario_actual)):
    solicitud = solicitud_crud.get_solicitud(db, id_solicitud)
    if not solicitud:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return solicitud

@router.post("/", response_model=schemas.SolicitudResponse, status_code=status.HTTP_201_CREATED)
def create_solicitud(solicitud: schemas.SolicitudCreate, db: Session = Depends(get_db), usuario_actual: dict = Depends(obtener_usuario_actual)):
    return solicitud_crud.create_solicitud(db, solicitud)

@router.put("/{id_solicitud}", response_model=schemas.SolicitudResponse)
def update_solicitud(id_solicitud: int, solicitud: schemas.SolicitudUpdate, db: Session = Depends(get_db), usuario_actual: dict = Depends(obtener_usuario_actual)):
    updated_solicitud = solicitud_crud.update_solicitud(db, id_solicitud, solicitud)
    if not updated_solicitud:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return updated_solicitud

@router.delete("/{id_solicitud}", status_code=status.HTTP_204_NO_CONTENT)
def delete_solicitud(id_solicitud: int, db: Session = Depends(get_db), usuario_actual: dict = Depends(obtener_usuario_actual)):
    deleted = solicitud_crud.delete_solicitud(db, id_solicitud)
    if not deleted:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return None