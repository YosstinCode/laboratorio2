from fastapi import APIRouter

from services.dispositivo_service import Dispositivo_service
from schemas.DispositivoDTO import Create_dispositivoDTO, Update_dispositivoDTO

dispositivos_router = APIRouter()
dispositivo_service = Dispositivo_service()

@dispositivos_router.get("/")
async def get_all_dispositivos():
    return dispositivo_service.get_all()


@dispositivos_router.post("/")
async def create_dispositivo_route(dispositivo: Create_dispositivoDTO):
    return dispositivo_service.create(dispositivo)


@dispositivos_router.get("/{dispositivo_id}")
async def get_one_dispositivos(dispositivo_id: int):
    return dispositivo_service.get_one(dispositivo_id)


@dispositivos_router.put("/{dispositivo_id}")
async def update_dispositivo_route(dispositivo_id: int, dispositivo_updated: Update_dispositivoDTO):
    return dispositivo_service.update(dispositivo_id, dispositivo_updated)


@dispositivos_router.delete("/{dispositivo_id}")
async def delete_dispositivo_route(dispositivo_id: int):
    return dispositivo_service.delete(dispositivo_id)
