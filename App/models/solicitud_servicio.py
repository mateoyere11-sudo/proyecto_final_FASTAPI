from datetime import date

from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base


class Solicitud(Base):
    __tablename__ = "solicitudes"
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, nullable=False)
    cliente = Column(String(255), nullable=False)
    servicio_id = Column(Integer, ForeignKey("Servicios.id"), nullable=False)
    servicio = relationship("Servicio", back_populates="solicitudes")