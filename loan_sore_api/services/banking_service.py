import re
from config.constants import COMMERCIAL_BANKS, MOBILE_LOAN_PROVIDERS

class BankingService:
    def __init__(self):
        pass
    
    def detect_bank_transactions(self, df):
        """Detect transactions from all banks"""
        # Your existing detect_bank_transactions function
        pass
    
    def analyze_specific_bank_transactions(self, df, bank_name):
        """Analyze transactions for a specific bank"""
        # Your existing function
        pass
    
    def get_all_banks(self):
        """Get all banks categorized"""
        # Your existing categorization logic
        pass

# Global instance
banking_service = BankingService()