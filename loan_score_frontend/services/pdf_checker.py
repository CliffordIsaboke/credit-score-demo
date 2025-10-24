import PyPDF2
import logging

logger = logging.getLogger(__name__)

class PDFChecker:
    @staticmethod
    def check_password_protection(file_path):
        """Check if PDF is password protected"""
        try:
            logger.info(f"Checking PDF encryption for: {file_path}")
            with open(file_path, 'rb') as f:
                pdf_reader = PyPDF2.PdfReader(f)
                is_encrypted = pdf_reader.is_encrypted
                logger.info(f"PDF is encrypted: {is_encrypted}")
                return is_encrypted
        except Exception as e:
            logger.error(f"Error checking PDF encryption: {e}")
            return False
    
    @staticmethod
    def test_password(file_path, password):
        """Test if password works for PDF"""
        try:
            with open(file_path, 'rb') as f:
                pdf_reader = PyPDF2.PdfReader(f)
                if pdf_reader.is_encrypted:
                    return pdf_reader.decrypt(password)
            return True
        except Exception as e:
            logger.error(f"Error testing PDF password: {e}")
            return False