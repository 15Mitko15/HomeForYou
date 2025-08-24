from fastapi import FastAPI
from src.routes import authRouter, propertyRouter, cityRouter, neighborhood
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="HomeForYou API",
    description="API for a real estate application.",
    version="1.0.0",
)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Authorization"],
)

app.include_router(authRouter.router)
app.include_router(propertyRouter.router)
app.include_router(cityRouter.router)
app.include_router(neighborhood.router)


@app.get("/")
def read_root():
    """Root endpoint."""
    return {"message": "Welcome to the HomeForYou API"}
