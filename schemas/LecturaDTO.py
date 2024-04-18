from pydantic import BaseModel
from typing import Optional, List

# from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
# from sqlalchemy.orm import relationship
# from config.database import Base_table

# class Lecturas(Base_table):
#     __tablename__ = 'lecturas'

#     id = Column(Integer, primary_key=True, index=True, autoincrement=True, name="id_lectura")
#     fecha_hora = Column(DateTime, nullable=False, name="fecha_hora")
#     valor = Column(String(100), nullable=False, name="valor")
#     sensor_id = Column(Integer, ForeignKey('sensores.id_sensor'), nullable=False, name="sensor_id")
#     sensor = relationship("Sensores", backref="lecturas", lazy=True)
#     tipo_lectura_id = Column(Integer, ForeignKey('tipo_lectura.id_tipo_lectura'), nullable=False, name="tipo_lectura_id")
#     tipo_lectura = relationship("Tipo_lectura", backref="lecturas", lazy=True)


class LecturaDTO(BaseModel):
    id_lectura: Optional[int] = None
    fecha_hora: str
    valor: str
    sensor_id: int
    tipo_lectura_id: int

class Create_lecturaDTO(BaseModel):
    fecha_hora: str
    valor: str
    sensor_id: int
    tipo_lectura_id: int

class Update_lecturaDTO(BaseModel):
    fecha_hora: Optional[str] = None
    valor: Optional[str] = None
    sensor_id: Optional[int] = None
    tipo_lectura_id: Optional[int] = None