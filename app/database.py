from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy_utils import database_exists,create_database

Base = declarative_base()
URL = "postgresql://postgres:admin@localhost:5432/Luqman"

if not database_exists(URL):
    create_database(URL)
    
engine = create_engine(URL , pool_size= 50 , echo= False)
SessionLocal = sessionmaker(autoflush= False, autocommit= False , bind= engine)

def get_db():
    db = SessionLocal()
    try : 
        yield db
    finally:
        db.close()
