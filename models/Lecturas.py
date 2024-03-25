from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base_table

class Lecturas(Base_table):
    __tablename__ = 'lecturas'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, name="id_lectura")
    fecha_hora = Column(String(100), nullable=False, name="fecha_hora")
    valor = Column(String(100), nullable=False, name="valor")
    sensor_id = Column(Integer, ForeignKey('sensores.id_sensor'), nullable=False, name="sensor_id")
