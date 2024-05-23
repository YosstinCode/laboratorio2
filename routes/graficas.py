from fastapi import APIRouter
from services.graficas_service import Graficas_service
from services.Tipo_lectura_service import Tipo_lectura_service

graficas_router = APIRouter()
graficas_service = Graficas_service()
tipo_lectura_service = Tipo_lectura_service()


@graficas_router.get("/linear/type/{type}")
def get_data_to_linear_graph(type: str, limit: int = 1):

    return graficas_service.get_last_by_type_with_limit(type, limit)
