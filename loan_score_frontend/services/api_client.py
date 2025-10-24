import requests
import json
import logging
from config.settings import API_BASE_URL, TIMEOUT

logger = logging.getLogger(__name__)

class APIClient:
    def __init__(self):
        self.base_url = API_BASE_URL
        self.timeout = TIMEOUT
    
    def check_connection(self):
        """Check API server connectivity"""
        try:
            response = requests.get(f"{self.base_url}/", timeout=5)
            if response.status_code == 200:
                # Try status endpoint for detailed info
                status_response = requests.get(f"{self.base_url}/status", timeout=5)
                if status_response.status_code == 200:
                    data = status_response.json()
                    return data.get('system_active', False), data.get('message', ''), True
                else:
                    return True, "API is running but status endpoint unavailable", True
            else:
                return False, f"API returned HTTP {response.status_code}", False
        except requests.exceptions.ConnectionError:
            return False, "Cannot connect to API server - check if server is running", False
        except requests.exceptions.Timeout:
            return False, "Connection timeout - server may be starting up", False
        except requests.exceptions.RequestException as e:
            return False, f"Network error: {str(e)}", False
        except Exception as e:
            return False, f"Unexpected error: {str(e)}", False
    
    def upload_pdf(self, file_path, loan_amount, password=None):
        """Upload PDF for analysis"""
        try:
            # Prepare request data
            files = {'file': (file_path.name, open(file_path, 'rb'), 'application/pdf')}
            data = {'loan_amount': str(loan_amount)}
            
            if password:
                data['password'] = password
            
            # Send request
            response = requests.post(
                f"{self.base_url}/analyze",
                files=files,
                data=data,
                timeout=self.timeout
            )
            
            # Close file handle
            files['file'][1].close()
            
            return self._handle_response(response)
            
        except Exception as e:
            logger.error(f"Upload error: {e}")
            raise
    
    def _handle_response(self, response):
        """Handle API response with proper error handling"""
        logger.info(f"Response status: {response.status_code}")
        
        if response.status_code == 200:
            return self._parse_success_response(response)
        elif response.status_code == 400:
            return self._handle_bad_request(response)
        elif response.status_code == 422:
            return self._handle_validation_error(response)
        elif response.status_code == 413:
            raise Exception("PDF file is too large for the server to process")
        elif response.status_code == 415:
            raise Exception("Invalid file type. Please upload a PDF file.")
        elif response.status_code >= 500:
            raise Exception(f"Server error (HTTP {response.status_code}). Please check server logs.")
        else:
            return self._handle_other_errors(response)
    
    def _parse_success_response(self, response):
        """Parse successful response"""
        try:
            result = response.json()
        except json.JSONDecodeError:
            result = self._safe_json_parse(response.text)
            if 'error' in result:
                raise Exception(result['error'])
        
        if result.get('success'):
            return result
        else:
            error_msg = result.get('error', 'Unknown error from API')
            raise Exception(f"API returned error: {error_msg}")
    
    def _handle_bad_request(self, response):
        """Handle 400 Bad Request"""
        try:
            error_data = response.json()
            detail = error_data.get('detail', 'Bad request')
            if 'password' in detail.lower() or 'encrypted' in detail.lower():
                raise PasswordRequiredError(detail)
            else:
                raise Exception(f"Bad request: {detail}")
        except:
            raise Exception(f"Bad request (HTTP 400): {response.text}")
    
    def _handle_validation_error(self, response):
        """Handle 422 Validation Error"""
        try:
            error_data = response.json()
            detail = error_data.get('detail', 'Validation error')
            raise Exception(f"Validation error: {detail}")
        except:
            raise Exception(f"Validation error (HTTP 422): {response.text}")
    
    def _handle_other_errors(self, response):
        """Handle other HTTP errors"""
        try:
            error_data = response.json()
            error_msg = error_data.get('detail', response.text)
        except:
            error_msg = response.text
        raise Exception(f"HTTP Error {response.status_code}: {error_msg}")
    
    def _safe_json_parse(self, response_text):
        """Safely parse JSON response"""
        try:
            return json.loads(response_text)
        except json.JSONDecodeError:
            if response_text.strip().startswith('<!DOCTYPE') or '<html' in response_text.lower():
                return {"error": "Server returned HTML error page - check server logs"}
            elif not response_text.strip():
                return {"error": "Empty response from server"}
            else:
                return {"error": f"Invalid JSON response: {response_text[:100]}..."}

class PasswordRequiredError(Exception):
    """Exception for password-protected PDFs"""
    pass