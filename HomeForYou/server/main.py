"""Main module for starting the project"""

from src.database import engine, Base

Base.metadata.create_all(bind=engine)
