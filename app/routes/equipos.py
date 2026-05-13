from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models.equipo import Equipo
from app.models.equipo_schema import EquipoCreate, EquipoResponse, EstadoUpdate, HistorialResponse
from typing import List, Optional
from app.models.historial import HistorialEstado



router = APIRouter()

#Dependencias para DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/equipos", response_model = EquipoResponse)
def crear_equipo(equipo: EquipoCreate, db: Session = Depends(get_db)):

    #Primero validar duplicado
    equipo_existente = db.query(Equipo).filter(
        Equipo.numero_serie == equipo.numero_serie
    ).first()

    if equipo_existente:
        raise HTTPException(
            status_code = 400,
            detail = "Ya existe un equipo con este número de serie"
        )

    nuevo_equipo = Equipo (
        nombre = equipo.nombre,
        marca = equipo.marca,
        modelo = equipo.modelo,
        numero_serie = equipo.numero_serie,
        estado = equipo.estado,
        es_critico = equipo.es_critico,
)
    db.add(nuevo_equipo)
    db.commit()
    db.refresh(nuevo_equipo)
    return nuevo_equipo

@router.get("/equipos", response_model=List[EquipoResponse])
def listar_equipos(
    estado: Optional[str] = None,
    es_critico: Optional[bool] = None,
    db: Session = Depends(get_db)
    ):

    query = db.query(Equipo)

#Filtro por estado
    if estado:
        query = query.filter(Equipo.estado == estado)

#Filtro por criticidad
    if es_critico is not None:
        query = query.filter(Equipo.es_critico == es_critico)

    equipos = query.all()
    return equipos

#Función put para actualizar registros (estado del equipo)
@router.put("/equipos/{equipo_id}/estado",response_model=EquipoResponse)
def actulizar_estado_equipo(
    equipo_id: int,
    datos: EstadoUpdate,
    db: Session = Depends(get_db)
):
    equipo = db.query(Equipo).filter(Equipo.id == equipo_id).first()

    if not equipo:
        raise HTTPException(
            status_code = 404,
            detail = "Equipo no encontrado"
        )
    
    estado_anterior = equipo.estado

    equipo.estado = datos.estado

    historial = HistorialEstado(
        equipo_id = equipo.id,
        estado_anterior = estado_anterior,
        estado_nuevo = datos.estado
    )

    db.add(historial)

    db.commit()
    db.refresh(equipo)

    return equipo

@router.get("/historial", response_model=List[HistorialResponse])
def listar_historial(db: Session = Depends(get_db)):
    historial = db.query(HistorialEstado).all()
    return historial
