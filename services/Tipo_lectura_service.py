from models.Tipo_lectura import Tipo_lectura
from services.CRUD import CRUD

class Tipo_lectura_service(CRUD):
    
    def __init__(self):        
        super().__init__(Tipo_lectura)