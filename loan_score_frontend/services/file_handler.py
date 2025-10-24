import os
import tempfile
from tkinter import filedialog
from config.settings import FILE_TYPES

class FileHandler:
    @staticmethod
    def select_pdf_file():
        """Open file dialog to select PDF"""
        file_path = filedialog.askopenfilename(filetypes=FILE_TYPES)
        return file_path
    
    @staticmethod
    def save_results(result_text, default_name="loan_analysis_results.txt"):
        """Save results to file"""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt", 
            filetypes=[("Text files", "*.txt")],
            initialfile=default_name
        )
        
        if file_path:
            try:
                with open(file_path, "w", encoding='utf-8') as file:
                    file.write(result_text)
                return True, file_path
            except Exception as e:
                return False, str(e)
        return False, "Save cancelled"
    
    @staticmethod
    def validate_file(file_path):
        """Validate PDF file"""
        if not os.path.exists(file_path):
            return False, "File not found"
        
        if os.path.getsize(file_path) == 0:
            return False, "PDF file is empty"
        
        if not file_path.lower().endswith('.pdf'):
            return False, "Please select a PDF file"
        
        return True, "Valid file"