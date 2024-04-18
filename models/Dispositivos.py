from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base_table

class Dispositivos(Base_table):
    __tablename__ = 'dispositivos'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, name="id_dispositivo")
    W = Column(String(20), nullable=False, name="w")
    N = Column(String(20), nullable=False, name="n")
    caracteristica_incubacion_id = Column(Integer, ForeignKey("caracteristicas_incubacion.id_caracteristicas_incubacion"), nullable=False, name="caracteristica_incubacion_id")
    caracteristica_incubacion = relationship("Caracteristicas_incubacion", backref="dispositivos", lazy=True)
