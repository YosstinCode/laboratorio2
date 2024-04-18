from models.Tipo_estado_alerta import Tipo_estado_alerta
from services.CRUD import CRUD

class Tipo_estado_alerta_service(CRUD):
    
    def __init__(self):        
        super().__init__(Tipo_estado_alerta)