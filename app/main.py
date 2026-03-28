from fastapi import FastAPI
from app.database import Base, engine
from app.models import Crypto
from app import crud

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(crud.router)

