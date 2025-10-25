from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from config.settings import MAX_CONCURRENT_USERS, UVICORN_WORKERS
from database.connection import db_manager
from services.ml_service import ml_service
from routers import analysis, banking, system

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print(f"Starting Loan Scoring API for {MAX_CONCURRENT_USERS} concurrent users...")
    
    # Load ML model
    ml_service.load_model()
    
    # Initialize database
    db = db_manager.get_database()
    if db:
        print("✓ MongoDB connection verified")
    
    yield
    
    # Shutdown
    print("Shutting down application...")

# Create FastAPI app
app = FastAPI(
    title="Loan Scoring API",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(system.router)
app.include_router(analysis.router)
app.include_router(banking.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        workers=UVICORN_WORKERS,
        log_level="info"
    )