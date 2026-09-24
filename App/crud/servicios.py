from sqlalchemy.orm import Session

from ..models.servicios import Servicio
from ..Schemas.servicio import ServicioCreate, ServicioUpdate


def get_servicios(db: Session):
    return db.query(Servicio).all()


def get_servicio(db: Session, id_servicio: int):
    return db.query(Servicio).filter(Servicio.id == id_servicio).first()


def create_servicio(db: Session, servicio: ServicioCreate):
    new_servicio = Servicio(**servicio.model_dump())
    db.add(new_servicio)
    db.commit()
    db.refresh(new_servicio)
    return new_servicio


def update_servicio(db: Session, id_servicio: int, servicio_data: ServicioUpdate):
    db_servicio = get_servicio(db, id_servicio)
    if not db_servicio:
        return None
    for key, value in servicio_data.model_dump(exclude_unset=True).items():
        setattr(db_servicio, key, value)
    db.commit()
    db.refresh(db_servicio)
    return db_servicio


def delete_servicio(db: Session, id_servicio: int):
    db_servicio = get_servicio(db, id_servicio)
    if not db_servicio:
        return None
    db.delete(db_servicio)
    db.commit()
    return db_servicio