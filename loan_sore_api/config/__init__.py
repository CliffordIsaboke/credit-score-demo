"""
Configuration module for Loan Scoring API
Environment variables, constants, and settings
"""

from .settings import *
from .constants import *

__all__ = [
    # From settings.py
    'MAX_CONCURRENT_USERS',
    'UVICORN_WORKERS', 
    'THREAD_POOL_WORKERS',
    'PROCESS_POOL_WORKERS',
    'MONGODB_URI',
    'DB_NAME',
    'COLLECTION_NAME',
    'RESULTS_COLLECTION',
    'CLIENTS_COLLECTION',
    'MODEL_PATH',
    'FEATURES_PATH',
    
    # From constants.py
    'MOBILE_LOAN_PROVIDERS',
    'COMMERCIAL_BANKS',
    'BETTING_COMPANIES',
    'SUPERMARKETS',
    'PETROL_STATIONS',
    'SHOPPING_MALLS',
    'HOSPITALS_MEDICAL',
    'RESTAURANTS_EATERIES',
    'UTILITY_PAYMENTS',
    'EDUCATION_INSTITUTIONS',
    'TRANSPORT_TRAVEL',
    'ENTERTAINMENT_LEISURE'
]