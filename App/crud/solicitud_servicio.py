from sqlalchemy.orm import Session, joinedload

from ..models.solicitud_servicio import Solicitud
from ..Schemas.solicitud import SolicitudCreate, SolicitudUpdate


def get_solicitudes(db: Session):
    return db.query(Solicitud).options(joinedload(Solicitud.servicio)).all()


def get_solicitud(db: Session, id_solicitud: int):
    return (
        db.query(Solicitud)
        .options(joinedload(Solicitud.servicio))
        .filter(Solicitud.id == id_solicitud)
        .first()
    )


def create_solicitud(db: Session, solicitud: SolicitudCreate):
    new_solicitud = Solicitud(**solicitud.model_dump())
    db.add(new_solicitud)
    db.commit()
    db.refresh(new_solicitud)
    return get_solicitud(db, new_solicitud.id)


def update_solicitud(db: Session, id_solicitud: int, solicitud_data: SolicitudUpdate):
    db_solicitud = get_solicitud(db, id_solicitud)
    if not db_solicitud:
        return None

    update_data = solicitud_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        if value is not None:
            setattr(db_solicitud, key, value)

    db.commit()
    db.refresh(db_solicitud)
    return get_solicitud(db, id_solicitud)


def delete_solicitud(db: Session, id_solicitud: int):
    db_solicitud = get_solicitud(db, id_solicitud)
    if not db_solicitud:
        return None

    db.delete(db_solicitud)
    db.commit()
    return db_solicitud