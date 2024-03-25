from models.Dispositivos import Dispositivos
from schemas.DispositivoDTO import CreateDispositivoDTO, UpdateDispositivoDTO
from services.CRUD import CRUD

class DispositivoService(CRUD):
    
    def __init__(self):        
        super().__init__(Dispositivos)
    