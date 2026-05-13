from pydantic import BaseModel, ConfigDict
from datetime import datetime


class EquipoCreate(BaseModel):
    nombre: str
    marca: str
    modelo: str
    numero_serie: str
    estado: str
    es_critico: bool

class EquipoResponse(BaseModel):
    id: int
    nombre: str
    marca: str
    modelo: str
    numero_serie: str
    estado: str
    es_critico: bool

    model_config = ConfigDict(from_attributes=True)

class EstadoUpdate(BaseModel):
    estado: str

class HistorialResponse(BaseModel):
    id: int
    equipo_id: int
    estado_anterior: str
    estado_nuevo: str
    fecha: datetime

    model_config = ConfigDict(from_attributes=True)
    
