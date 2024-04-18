from models.Estados_huevos import Estados_huevos
from services.CRUD import CRUD

class Estados_huevos_service(CRUD):
    
    def __init__(self):        
        super().__init__(Estados_huevos)
