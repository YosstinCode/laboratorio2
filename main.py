from fastapi import FastAPI
from routes.sensor import sensor_router
from routes.dispositivos import dispositivos_router
from routes.lecturas import lecturas_router
from config.database import engine, Base_table

# Crear las tablas en la DB
Base_table.metadata.create_all(engine) 

# iniciar con el comando: uvicorn main:app --reload --port 3000
app = FastAPI(root_path="/api/v1")

app.include_router(sensor_router, prefix="/sensores", tags=["Sensores"])
app.include_router(dispositivos_router, prefix="/dispositivos", tags=["Dispositivos"])
app.include_router(lecturas_router, prefix="/lecturas", tags=["Lecturas"])
