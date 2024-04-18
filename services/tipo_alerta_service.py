from models.Tipo_alerta import Tipo_alerta
from services.CRUD import CRUD

class Tipo_alerta_service(CRUD):
    
    def __init__(self):        
        super().__init__(Tipo_alerta)