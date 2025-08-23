# src/main.py

from fastapi import FastAPI
from src.routes import authRouter

# Create the FastAPI app instance
app = FastAPI(
    title="HomeForYou API",
    description="API for a real estate application.",
    version="1.0.0",
)

# Include your authentication router
app.include_router(authRouter.router)


# Optional: Add a root endpoint to easily check if the server is running
@app.get("/")
def read_root():
    """Root endpoint."""
    return {"message": "Welcome to the HomeForYou API"}
