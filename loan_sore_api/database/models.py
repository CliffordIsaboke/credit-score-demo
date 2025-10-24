from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class AnalysisRequest(BaseModel):
    loan_amount: float

class BankInfo(BaseModel):
    bank_name: str
    transaction_count: int
    total_inflow: float
    total_outflow: float
    net_flow: float

class AnalysisResponse(BaseModel):
    success: bool
    result_id: Optional[str] = None
    results: List[Dict[str, Any]]
    error: Optional[str] = None
    client_info: Dict[str, Any]
    score: float
    eligible: bool
    analysis_count: Optional[int] = 0
    bank_activity: List[BankInfo] = []

class SystemStatus(BaseModel):
    system_active: bool
    message: str
    db_connected: bool

class BankAnalysisResponse(BaseModel):
    bank_name: str
    transactions_found: int
    # ... your bank analysis fields