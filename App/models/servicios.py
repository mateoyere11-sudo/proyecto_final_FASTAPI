from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base


class Servicio(Base):
    __tablename__ = "Servicios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False, unique=True)
    precio = Column(Integer, nullable=False)
    solicitudes = relationship("Solicitud", back_populates="servicio")