from fastapi import APIRouter

from services.Caracteristicas_incubacion_service import Caracteristicas_incubacion_service
from schemas.Caracteristicas_incubacionDTO import Create_caracteristicas_incubacionDTO, Update_caracteristicas_incubacionDTO

caracteristicas_incubacion_router = APIRouter()
caracteristicas_incubacion_service = Caracteristicas_incubacion_service()

@caracteristicas_incubacion_router.get("/")
async def get_all_caracteristicas_incubacion():
    return caracteristicas_incubacion_service.get_all()


@caracteristicas_incubacion_router.post("/")
async def create_caracteristicas_incubacion_route(caracteristicas_incubacion: Create_caracteristicas_incubacionDTO):
    return caracteristicas_incubacion_service.create(caracteristicas_incubacion)


@caracteristicas_incubacion_router.get("/{caracteristicas_incubacion_id}")
async def get_one_caracteristicas_incubacions(caracteristicas_incubacion_id: int):
    return caracteristicas_incubacion_service.get_one(caracteristicas_incubacion_id)


@caracteristicas_incubacion_router.put("/{caracteristicas_incubacion_id}")
async def update_caracteristicas_incubacion_route(caracteristicas_incubacion_id: int, caracteristicas_incubacion_updated: Update_caracteristicas_incubacionDTO):
    return caracteristicas_incubacion_service.update(caracteristicas_incubacion_id, caracteristicas_incubacion_updated)


@caracteristicas_incubacion_router.delete("/{caracteristicas_incubacion_id}")
async def delete_caracteristicas_incubacion_route(caracteristicas_incubacion_id: int):
    return caracteristicas_incubacion_service.delete(caracteristicas_incubacion_id)