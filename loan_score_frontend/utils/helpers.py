import logging
import sys

def setup_logging():
    """Setup application logging"""
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def center_window(window):
    """Center any window on screen"""
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

def format_loan_score_guide():
    """Format the loan score guide text"""
    return (
        "Score Range  | Interpretation         | Eligibility\n"
        "-------------| ---------------------- | -----------\n"
        " 0 -30%      | Low risk (good client) |  Yes\n"
        "30 -70%      | Moderate risk          |  Yes\n"
        "70 -100%     | High risk              |   No"
    )