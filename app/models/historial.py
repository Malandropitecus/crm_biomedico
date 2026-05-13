from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.database.database import Base

class HistorialEstado(Base):
    __tablename__ = "historial_estados"

    id = Column(Integer, primary_key=True, index=True)
    equipo_id = Column(Integer, ForeignKey("equipos.id"))
    estado_anterior = Column(String)
    estado_nuevo = Column(String)
    fecha = Column(DateTime, default=datetime.utcnow)
    
        
