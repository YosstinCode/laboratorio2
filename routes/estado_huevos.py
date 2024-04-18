from fastapi import APIRouter

from services.estado_huevos_service import Estados_huevos_service
from schemas.Estados_huevosDTO import Create_estados_huevosDTO, Update_estados_huevosDTO

estados_huevos_router = APIRouter()
estados_huevos_service = Estados_huevos_service()

@estados_huevos_router.get("/")
async def get_all_estados_huevos():
    return estados_huevos_service.get_all()


@estados_huevos_router.post("/")
async def create_estados_huevos_route(estados_huevos: Create_estados_huevosDTO):
    return estados_huevos_service.create(estados_huevos)


@estados_huevos_router.get("/{estados_huevos_id}")
async def get_one_estados_huevoss(estados_huevos_id: int):
    return estados_huevos_service.get_one(estados_huevos_id)


@estados_huevos_router.put("/{estados_huevos_id}")
async def update_estados_huevos_route(estados_huevos_id: int, estados_huevos_updated: Update_estados_huevosDTO):
    return estados_huevos_service.update(estados_huevos_id, estados_huevos_updated)


@estados_huevos_router.delete("/{estados_huevos_id}")
async def delete_estados_huevos_route(estados_huevos_id: int):
    return estados_huevos_service.delete(estados_huevos_id)