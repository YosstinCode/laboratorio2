from fastapi import APIRouter
from services.tipo_ave_service import Tipo_ave_service
from schemas.Tipo_aveDTO import Create_tipo_aveDTO, Update_tipo_aveDTO

tipo_ave_router = APIRouter()
tipo_ave_service = Tipo_ave_service()

@tipo_ave_router.get("/")
async def get_all_tipo_ave():
    return tipo_ave_service.get_all()

@tipo_ave_router.get("/{tipo_ave_id}")
async def get_one_tipo_ave(tipo_ave_id: int):
    return tipo_ave_service.get_one(tipo_ave_id)

@tipo_ave_router.post("/")
async def create_tipo_ave(tipo_ave: Create_tipo_aveDTO):
    return tipo_ave_service.create(tipo_ave)

@tipo_ave_router.put("/{tipo_ave_id}")
async def update_tipo_ave(tipo_ave_id: int, tipo_ave: Update_tipo_aveDTO):
    return tipo_ave_service.update(tipo_ave_id, tipo_ave)

@tipo_ave_router.delete("/{tipo_ave_id}")
async def delete_tipo_ave(tipo_ave_id: int):
    return tipo_ave_service.delete(tipo_ave_id)