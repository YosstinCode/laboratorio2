from sqlalchemy import Column, Integer, String
from config.database import Base_table

class Estado_alerta(Base_table):
    __tablename__ = 'estado_alerta'
    
    id_estado_alerta = Column(Integer, primary_key=True, name="id_estado_alerta")
    nombre = Column(String(50), nullable=False, name="nombre")
    