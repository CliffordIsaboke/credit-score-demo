"""
Loan Scoring API
FastAPI backend for M-Pesa statement analysis and loan scoring
"""

__version__ = "1.0.0"
__author__ = "Clifford Isaboke"
__description__ = "API for analyzing M-Pesa statements and calculating loan scores"

# Import main app for easier access
from .main import app

__all__ = ['app']