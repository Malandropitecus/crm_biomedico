from sqlalchemy import Column, Integer, String, Boolean
from app.database.database import Base

class Equipo(Base):
    __tablename__ = "equipos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    marca = Column(String)
    modelo = Column(String)
    numero_serie = Column(String, unique=True)
    estado = Column(String)
    es_critico = Column(Boolean, default=False)
    