from fastapi import APIRouter
from database.models import SystemStatus
from database.connection import db_manager
from utils.helpers import check_system_status

router = APIRouter(prefix="/system", tags=["system"])

@router.get("/status", response_model=SystemStatus)
async def get_system_status():
    """Get system status"""
    system_ok, message = check_system_status()
    db_connected = db_manager.check_connection()
    
    return SystemStatus(
        system_active=system_ok,
        message=message,
        db_connected=db_connected
    )

@router.get("/")
async def root():
    return {"message": "Loan Scoring API", "version": "1.0.0"}