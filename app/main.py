from fastapi import FastAPI
from app.database.database import engine, Base
from app.models import equipo, historial
from app.routes import equipos
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

#Permisos para conectar el frontend y el backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Crear tablas
Base.metadata.create_all(bind=engine)

app.include_router(equipos.router)

@app.get("/")
def home():
    return {"Mensaje":"CRM Biomédico funcionando"}