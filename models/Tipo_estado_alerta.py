from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base_table

class Tipo_estado_alerta(Base_table):
    __tablename__ = 'tipo_estado_alerta'
    
    id_tipo_estado_alerta = Column(Integer, primary_key=True, index=True, autoincrement=True, name="id_tipo_estado_alerta")
    estado_alerta_id = Column(Integer, ForeignKey('estado_alerta.id_estado_alerta'), nullable=False, name="estado_alerta_id")
    tipo_alerta_id = Column(Integer, ForeignKey('tipo_alerta.id_tipo_alerta'), nullable=False, name="tipo_alerta_id")
    estado_alerta = relationship("Estado_alerta", backref="tipo_estado_alerta", lazy=True)
    tipo_alerta = relationship("Tipo_alerta", backref="tipo_estado_alerta", lazy=True)
