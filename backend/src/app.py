from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import scan, phishing
from .database import engine, Base
from . import models

# Create database tables if they don't exist
# This is useful if the init.sql script didn't run for some reason
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SafeEye API",
    description="Backend for SafeEye Cyber Security Tool",
    version="1.0.0"
)

# CORS Configuration
origins = [
    "http://localhost",
    "http://localhost:3000",
    "*"  # For development
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(scan.router, prefix="/scan", tags=["scan"])
app.include_router(phishing.router, prefix="/phishing", tags=["phishing"])

@app.get("/")
def read_root():
    return {"status": "online", "message": "SafeEye Backend is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
