from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
import pytz


class LecturaDTO(BaseModel):
    id_lectura: Optional[int] = None
    fecha_hora: str
    valor: str
    sensor_id: int
    tipo_lectura_id: int


class Create_lecturaDTO(BaseModel):
    fecha_hora: Optional[str] = None
    valor: str
    sensor_id: int
    tipo_lectura_id: int


class Update_lecturaDTO(BaseModel):
    fecha_hora: Optional[str] = None
    valor: Optional[str] = None
    sensor_id: Optional[int] = None
    tipo_lectura_id: Optional[int] = None
