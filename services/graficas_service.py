from config.database import SessionLocal
from services.lecturas_service import Lecturas_service


class Graficas_service:

    def __init__(self):
        self.db = SessionLocal()
        self.lecturas_service = Lecturas_service()

    def get_data(self):
        return self.lecturas_service.get_all()

    def get_data_by_type_and_date(self, type: int, date: str):
        data = self.lecturas_service.get_all_by_type_and_date(type, date)

        mapped_data = []

        for item in data:
            mapped_data.append({
                "x": item.fecha_hora,
                "y": item.valor
            })

        return mapped_data

    def get_last_by_type_with_limit(self, type: int, limit: int):
        data = self.lecturas_service.get_last_by_type_with_limit(type, limit)
        mapped_data = []

        for item in data:
            mapped_data.append({
                "x": item.fecha_hora,
                "y": item.valor
            })

        return mapped_data
