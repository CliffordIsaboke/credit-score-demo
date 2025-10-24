import customtkinter as ctk
from datetime import datetime

# API Configuration
API_BASE_URL = "http://127.0.0.1:8000"
# API_BASE_URL = "http://192.168.2.109:8000"
# API_BASE_URL = "http://165.227.148.232:8000"

# Color Scheme for Results Table
COLOR_SCHEME = {
    "financial_metrics": "#E8F5E9",
    "mobile_loans": "#E3F2FD",
    "repayment_frequency": "#FFF3E0",
    "betting_activity": "#FFEBEE",
    "suspicious_payments": "#F3E5F5",
    "section_header": "#00008B",
    "deposit_activity": "#E8F4F8",
    "duration_warning": "#FFF9C4",
}

# Application Constants
APP_TITLE = "Demulla Investment Limited - API Client"
COMPANY_NAME = "Powered by: Wiltac Solutions Limited"
DEFAULT_LOAN_AMOUNT = 10000.0
TIMEOUT = 120  # seconds

# File Types
FILE_TYPES = [("PDF files", "*.pdf")]