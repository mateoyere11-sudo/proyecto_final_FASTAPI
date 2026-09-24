from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..Schemas import servicio as schemas
from ..crud import servicios as servicio_crud
from ..database import get_db
from ..Auth import obtener_usuario_actual

router = APIRouter(prefix="/servicios", tags=["Servicios"])


@router.get("/", response_model=list[schemas.ServicioResponse])
def list_servicios(db: Session = Depends(get_db), usuario_actual: dict = Depends(obtener_usuario_actual)):
    return servicio_crud.get_servicios(db)


@router.get("/{id_servicio}", response_model=schemas.ServicioResponse)
def get_servicio(id_servicio: int, db: Session = Depends(get_db), usuario_actual: dict = Depends(obtener_usuario_actual)):
    servicio = servicio_crud.get_servicio(db, id_servicio)
    if not servicio:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Servicio no encontrado",
        )
    return servicio


@router.post("/", response_model=schemas.ServicioResponse, status_code=status.HTTP_201_CREATED)
def create_servicio(servicio: schemas.ServicioCreate, db: Session = Depends(get_db), usuario_actual: dict = Depends(obtener_usuario_actual)):
    return servicio_crud.create_servicio(db, servicio)


@router.put("/{id_servicio}", response_model=schemas.ServicioResponse)
def update_servicio(id_servicio: int, servicio: schemas.ServicioUpdate, db: Session = Depends(get_db), usuario_actual: dict = Depends(obtener_usuario_actual)):
    updated_servicio = servicio_crud.update_servicio(db, id_servicio, servicio)
    if not updated_servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return updated_servicio


@router.delete("/{id_servicio}", status_code=status.HTTP_204_NO_CONTENT)
def delete_servicio(id_servicio: int, db: Session = Depends(get_db), usuario_actual: dict = Depends(obtener_usuario_actual)):
    deleted = servicio_crud.delete_servicio(db, id_servicio)
    if not deleted:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return None