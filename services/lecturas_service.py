from models.Lecturas import Lecturas
from services.CRUD import CRUD
from sqlalchemy import desc


class Lecturas_service(CRUD):

    def __init__(self):
        super().__init__(Lecturas)

    def get_all_by_type_and_date(self, type=None, date=None):

        query = []

        if date and type:
            query = self.db.query(Lecturas).filter(
                Lecturas.fecha_hora == date,
                Lecturas.tipo_lectura_id == type
            ).all()

        return query

    def get_last_by_type_with_limit(self, type=None, limit=1):
        if type:
            query = self.db.query(Lecturas).filter(
                Lecturas.tipo_lectura_id == type
            ).order_by(desc(Lecturas.id)).limit(limit).all()
        else:
            query = None

        return query
