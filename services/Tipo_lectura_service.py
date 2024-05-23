from models.Tipo_lectura import Tipo_lectura
from services.CRUD import CRUD


class Tipo_lectura_service(CRUD):

    def __init__(self):
        super().__init__(Tipo_lectura)

    def get_name_by_id(self, id):
        query = self.db.query(Tipo_lectura).filter(
            Tipo_lectura.id == id).first()
        return query.nombre
