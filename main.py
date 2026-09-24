from fastapi import FastAPI
from App.database import Base, engine
from App.Routers.auth import router as auth_router
from App.models import servicios, solicitud_servicio

Base.metadata.create_all(bind=engine)

app = FastAPI()

from App.Routers.servicios import router as servicios_router
from App.Routers.solicitud import router as solicitud_router

app.include_router(servicios_router)
app.include_router(solicitud_router)
app.include_router(auth_router)