from pydantic import BaseModel
from typing import Optional, List

class DispositivoDTO(BaseModel):
    id: int
    W: str
    N: str
    
class CreateDispositivoDTO(BaseModel):
    W: str
    N: str
    
class UpdateDispositivoDTO(BaseModel):
    W: Optional[str] = None
    N: Optional[str] = None