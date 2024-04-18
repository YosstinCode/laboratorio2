from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base_table

class Alertas(Base_table):
    __tablename__ = 'alertas'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, name="id_alertas")
    fecha_alertas = Column(DateTime, nullable=False, name="fecha_alertas")
    lectura_id = Column(Integer, ForeignKey('lecturas.id_lectura'), nullable=False, name="lectura_id")
    lectura = relationship("Lecturas", backref="alertas", lazy=True)
    tipo_estado_alerta_id = Column(Integer, ForeignKey('tipo_estado_alerta.id_tipo_estado_alerta'), nullable=False, name="tipo_estado_alerta_id")
    tipo_estado_alerta = relationship("Tipo_estado_alerta", backref="alertas", lazy=True)
