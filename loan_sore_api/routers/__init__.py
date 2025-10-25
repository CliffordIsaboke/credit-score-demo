"""
Routers module for Loan Scoring API
FastAPI route handlers and endpoints
"""

from .analysis import router as analysis_router
from .banking import router as banking_router
from .system import router as system_router

__all__ = [
    'analysis_router',
    'banking_router', 
    'system_router'
]

# Optional: Package-level router aggregation
from fastapi import APIRouter

# Create a main router that includes all sub-routers
api_router = APIRouter()
api_router.include_router(analysis_router, prefix="/api/v1", tags=["analysis"])
api_router.include_router(banking_router, prefix="/api/v1", tags=["banks"])
api_router.include_router(system_router, prefix="/api/v1", tags=["system"])

__all__.append('api_router')