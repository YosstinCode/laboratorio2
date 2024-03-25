from pydantic import BaseModel
from typing import Optional, List

class LecturaDTO(BaseModel):
    id: Optional[int]
    fecha_hora: str
    valor: str
    sensor_id: int