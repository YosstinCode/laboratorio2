from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from routes.Tipo_ave import tipo_ave_router
from routes.Alertas import alertas_router
from routes.caracteristicas_incubacion import caracteristicas_incubacion_router
from routes.dispositivos import dispositivos_router
from routes.estado_alerta import estado_alerta_router
from routes.estado_huevos import estados_huevos_router
from routes.huevos import huevos_router
from routes.lecturas import lecturas_router
from routes.revision_huevos import revision_huevos_router
from routes.sensor import sensor_router
from routes.Tipo_alerta import tipo_alerta_router
from routes.Tipo_ave import tipo_ave_router
from routes.Tipo_estado_alerta import tipo_estado_alerta_router
from routes.Tipo_lectura import tipo_lectura_router
from config.database import engine, Base_table

# Crear las tablas en la DB
Base_table.metadata.create_all(engine)

# iniciar con el comando: uvicorn main:app --reload --port 3000
app = FastAPI(root_path="/api/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sensor_router, prefix="/sensores", tags=["Sensores"])
app.include_router(dispositivos_router,
                   prefix="/dispositivos", tags=["Dispositivos"])
app.include_router(lecturas_router, prefix="/lecturas", tags=["Lecturas"])
app.include_router(huevos_router, prefix="/huevos", tags=["Huevos"])
app.include_router(revision_huevos_router,
                   prefix="/revision_huevos", tags=["Revision_huevos"])
app.include_router(estados_huevos_router,
                   prefix="/estados_huevos", tags=["Estados_huevos"])
app.include_router(alertas_router, prefix="/alertas", tags=["Alertas"])
app.include_router(estado_alerta_router,
                   prefix="/estado_alerta", tags=["Estado_alerta"])
app.include_router(tipo_alerta_router,
                   prefix="/tipo_alerta", tags=["Tipo_alerta"])
app.include_router(tipo_ave_router, prefix="/tipo_ave", tags=["Tipo_ave"])
app.include_router(tipo_estado_alerta_router,
                   prefix="/tipo_estado_alerta", tags=["Tipo_estado_alerta"])
app.include_router(tipo_lectura_router,
                   prefix="/tipo_lectura", tags=["Tipo_lectura"])
app.include_router(caracteristicas_incubacion_router,
                   prefix="/caracteristicas_incubacion", tags=["Caracteristicas_incubacion"])
