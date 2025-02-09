"""Main module for starting the project"""

from fastapi import FastAPI
from server.src.database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)
