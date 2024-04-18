from models.Dispositivos import Dispositivos
from services.CRUD import CRUD

class Dispositivo_service(CRUD):
    
    def __init__(self):        
        super().__init__(Dispositivos)
