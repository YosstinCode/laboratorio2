from models.Caracteristicas_incubacion import Caracteristicas_incubacion
from services.CRUD import CRUD

class Caracteristicas_incubacion_service(CRUD):
    
    def __init__(self):        
        super().__init__(Caracteristicas_incubacion)
