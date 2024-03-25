from fastapi import APIRouter
from services.sensor_service import SensorService
from schemas.SensorDTO import CreateSensorDTO, UpdateSensorDTO


sensor_router = APIRouter()
sensor_service = SensorService()

@sensor_router.get("/")
async def get_all_sensores():
    return sensor_service.get_all()

@sensor_router.get("/{sensor_id}")
async def get_one_sensor(sensor_id: int):
    return sensor_service.get_one(sensor_id)

@sensor_router.post("/")
async def create_sensor(sensor: CreateSensorDTO):
    return sensor_service.create(sensor)

@sensor_router.put("/{sensor_id}")
async def update_sensor(sensor_id: int, sensor: UpdateSensorDTO):
    return sensor_service.update(sensor_id, sensor)

@sensor_router.delete("/{sensor_id}")
async def delete_sensor(sensor_id: int):
    return sensor_service.delete(sensor_id)





