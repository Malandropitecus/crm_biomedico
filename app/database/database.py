from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Ruta de la base de datos SQLite
DATABASE_URL = "sqlite:///./crm.db"

#Crear engine
engine = create_engine (
    DATABASE_URL, connect_args={"check_same_thread":False}
)

#Crear sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base para modelos
Base = declarative_base()
