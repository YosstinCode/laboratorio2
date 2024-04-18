from models.Estado_alerta import Estado_alerta
from services.CRUD import CRUD

class Estado_alerta_service(CRUD):
    
    def __init__(self):        
        super().__init__(Estado_alerta)
