from sqlalchemy import Column, Integer, String
from config.database import Base_table

class Tipo_alerta(Base_table):
    __tablename__ = 'tipo_alerta'
    
    id_tipo_alerta = Column(Integer, primary_key=True, index=True, autoincrement=True, name="id_tipo_alerta")
    nombre = Column(String(50), nullable=False, name="nombre")