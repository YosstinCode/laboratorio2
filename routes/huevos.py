from fastapi import APIRouter

from services.huevos_service import Huevos_service
from schemas.HuevosDTO import Create_huevosDTO, Update_huevosDTO

huevos_router = APIRouter()
huevos_service = Huevos_service()

@huevos_router.get("/")
async def get_all_huevos():
    return huevos_service.get_all()


@huevos_router.post("/")
async def create_huevos_route(huevos: Create_huevosDTO):
    return huevos_service.create(huevos)


@huevos_router.get("/{huevos_id}")
async def get_one_huevoss(huevos_id: int):
    return huevos_service.get_one(huevos_id)


@huevos_router.put("/{huevos_id}")
async def update_huevos_route(huevos_id: int, huevos_updated: Update_huevosDTO):
    return huevos_service.update(huevos_id, huevos_updated)


@huevos_router.delete("/{huevos_id}")
async def delete_huevos_route(huevos_id: int):
    return huevos_service.delete(huevos_id)