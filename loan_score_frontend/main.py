import customtkinter as ctk
import threading
import logging
from config.settings import APP_TITLE
from components.navigation import Header, Footer, GuidePanel
from components.table import ResultsTable
from components.progress import ProgressManager
from components.dialogs import CTkMessageBox, CTkInputDialog, PasswordDialog
from services.api_client import APIClient, PasswordRequiredError
from services.file_handler import FileHandler
from services.pdf_checker import PDFChecker
from utils.threading import ThreadManager
from utils.helpers import setup_logging, center_window
from config.settings import DEFAULT_LOAN_AMOUNT

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)

class LoanScoringApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title(APP_TITLE)
        self.geometry("1000x900")
        self.resizable(True, True)
        
        # Initialize services
        self.api_client = APIClient()
        self.file_handler = FileHandler()
        self.pdf_checker = PDFChecker()
        self.thread_manager = ThreadManager()
        
        # Application state
        self.result_data = []
        self.processing_cancelled = False
        
        # Setup UI
        self.setup_ui()
        self.initialize_application()
        
        # Make sure window is focused
        self.lift()
        self.attributes('-topmost', True)
        self.after_idle(lambda: self.attributes('-topmost', False))
    
    def setup_ui(self):
        """Setup the main user interface"""
        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)  # Table frame gets weight
        
        # Create components
        self.header = Header(self)
        self.progress_manager = ProgressManager(self)
        self.results_table = ResultsTable(self)
        self.footer = Footer(self)
        self.guide_panel = GuidePanel(self)
        
        # Layout components
        self.header.grid(row=0, column=0, sticky="ew", padx=15, pady=5)
        
        # Title
        self.title_label = ctk.CTkLabel(
            self,
            text="Loan Score",
            font=("Helvetica", 16, "bold"),
            text_color="#2c3e50"
        )
        self.title_label.grid(row=1, column=0, pady=(0, 10))
        
        # Progress frame (row 2 managed by ProgressManager)
        self.progress_manager.progress_frame.grid(row=2, column=0, sticky="ew", padx=20, pady=5)
        
        # Results table (row 3)
        self.results_table.grid(row=3, column=0, sticky="nsew", padx=20, pady=10)
        
        # Lower frame with buttons and guide
        self.setup_control_panel()
        
        # Footer (row 5)
        self.footer.grid(row=5, column=0, pady=10)
    
    def setup_control_panel(self):
        """Setup control panel with buttons and guide"""
        lower_frame = ctk.CTkFrame(self)
        lower_frame.grid(row=4, column=0, sticky="ew", padx=20, pady=15)
        lower_frame.grid_columnconfigure(1, weight=1)
        
        # Button frame (left)
        self.setup_buttons(lower_frame)
        
        # Guide panel (right)
        self.guide_panel.grid(row=0, column=1, sticky="ne", padx=30, pady=5)
    
    def setup_buttons(self, parent):
        """Setup action buttons"""
        button_frame = ctk.CTkFrame(parent, fg_color="transparent")
        button_frame.grid(row=0, column=0, sticky="nw", padx=10, pady=5)
        
        buttons = [
            ("📤 Upload PDF", self.upload_pdf_and_score, "#4CAF50", "bold"),
            ("💾 Save Results", self.save_results, "#2196F3", "normal"),
            ("🧹 Clear Table", self.clear_table, "#f44336", "normal"),
            ("❌ Cancel", self.cancel_processing, "#ff9800", "normal"),
            ("🌐 API Status", self.show_api_status, "#9C27B0", "normal"),
        ]
        
        for text, command, color, font_weight in buttons:
            btn = ctk.CTkButton(
                button_frame,
                text=text,
                command=command,
                width=150,
                height=35,
                fg_color=color,
                font=("Arial", 10, font_weight)
            )
            btn.pack(pady=2)
            
            # Store cancel button reference
            if text == "❌ Cancel":
                self.cancel_button = btn
                self.cancel_button.configure(state="disabled")
    
    # ... (Rest of the methods from your original class would go here)
    # I've shown the structure - you would continue with:
    # - upload_pdf_and_score
    # - process_pdf_with_api
    # - handle_password_requests
    # - etc.

    def upload_pdf_and_score(self):
        """Main upload handler - you would implement this"""
        pass
    
    def process_pdf_with_api(self, file_path, loan_amount, password=None):
        """Process PDF with API - you would implement this"""
        pass
    
    # ... and all other methods from your original class

if __name__ == "__main__":
    app = LoanScoringApp()
    app.mainloop()