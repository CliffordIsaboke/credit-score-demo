# Analysis System

A comprehensive full-stack application for analyzing M-Pesa statements and calculating loan eligibility scores using machine learning.

## Overview

The Loan Scoring System consists of:
- **Backend API**: FastAPI-based REST API for PDF processing and ML scoring
- **Frontend GUI**: CustomTkinter desktop application for user interaction
- **Machine Learning**: Random Forest model for credit risk assessment
- **Database**: MongoDB for storing analysis results and client information

### Key Capabilities

- Analyze M-Pesa statement PDFs
- Machine learning-powered credit scoring
- Detect banking and mobile loan transactions
- Identify spending patterns and financial behavior
- Calculate financial metrics and eligibility
- Save and manage analysis results

## Features

### Backend Features
- **High Performance**: Supports 100+ concurrent users
- **PDF Processing**: Advanced M-Pesa statement parsing
- **ML Integration**: Pre-trained credit scoring model
- **Bank Detection**: 100+ Kenyan banks and financial institutions
- **Transaction Analysis**: Categorizes spending patterns
- **RESTful API**: Comprehensive API endpoints
- **MongoDB Integration**: Scalable data storage
- **Async Processing**: Non-blocking PDF processing

### Frontend Features
- **Modern GUI**: CustomTkinter-based interface
- **Real-time Progress**: Animated progress indicators
- **Password Support**: Encrypted PDF handling
- **Results Export**: Save analysis to text files
- **Connection Monitoring**: Live API status updates
- **Responsive Design**: Adapts to different screen sizes


### Backend Structure

loan_scoring_api/
├── main.py                 # FastAPI app entry point
├── config/                 # Configuration settings
├── database/               # MongoDB models & connection
├── services/               # Business logic services
├── routers/                # API route handlers
└── utils/                  # Utility functions


### Frontend Structure

loan_scoring_frontend/
├── main.py                 # GUI application entry point
├── config/                 # App settings and styling
├── components/             # UI components
├── services/               # API clients and file handling
└── utils/                  # Helper functions


## Installation

### Prerequisites

- Python 3.8+
- MongoDB (local or cloud)
- Required Python packages

### Backend Installation

1. **Clone the repository**
   
   git clone https://github.com/CliffordIsaboke/mpesa-credit-score-demo.git
   cd loan_scoring_api
   

2. **Create virtual environment**
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   

3. **Install dependencies**
   pip install -r requirements.txt
   

4. **Set up environment variables**
   # Edit example.env with your MongoDB connection details
   

5. **Start MongoDB**
   # If using local MongoDB
   mongod --dbpath /path/to/data/directory

### Frontend Installation

1. **Navigate to frontend directory**
     cd loan_scoring_frontend

2. **Install dependencies**
   pip install -r requirements.txt
  

## Configuration

### Backend Configuration (.env)

# MongoDB Configuration
MONGODB_URI=mongodb://localhost:27017
DB_NAME=loan_scoring
COLLECTION_NAME=system_config
RESULTS_COLLECTION=analysis_results
CLIENTS_COLLECTION=clients

# Optional: Cloud MongoDB
- MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/


### Frontend Configuration

Update API URL in `config/settings.py`:
# Local development
API_BASE_URL = "http://127.0.0.1:8000"

# Production
# API_BASE_URL = "http://your-server-ip:8000"


## Usage

### Starting the Backend

1. **Navigate to backend directory**
   cd loan_scoring_api

2. **Start the FastAPI server**
   python main.py

   Or using uvicorn directly:
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload


3. **Verify server is running**
   - Open http://localhost:8000 in your browser
   - You should see the API documentation

### Starting the Frontend

1. **Navigate to frontend directory**
   cd loan_scoring_frontend

2. **Run the GUI application**
   python main.py

3. **Using the Application**
   - Click "Upload PDF" to select an M-Pesa statement
   - Enter the requested loan amount
   - Provide password if PDF is encrypted
   - View real-time analysis progress
   - Review results in the table

## API Documentation

### Base URL
http://localhost:8000


### Key Endpoints

#### Analysis Endpoints
- `POST /analyze` - Analyze PDF and calculate loan score
- `GET /status` - Check system status
- `GET /` - API information

#### Banking Endpoints
- `GET /banks` - List all supported banks
- `POST /analyze-bank` - Analyze specific bank transactions

### Example API Usage

# Check API status
curl http://localhost:8000/status

# Analyze PDF
curl -X POST -F "file=@statement.pdf" -F "loan_amount=50000" http://localhost:8000/analyze

### Request Format
{
  "file": "PDF file",
  "loan_amount": 50000.0,
  "password": "optional_password"
}

### Response Format
{
  "success": true,
  "result_id": "unique_id",
  "results": [
    {"metric": "Client Name", "value": "John Doe", "category": "basic_info"},
    # ... more results
  ],
  "client_info": {
    "name": "John Doe",
    "phone": "254712345678"
  },
  "score": 45.5,
  "eligible": true,
  "analysis_count": 150,
  "bank_activity": [
    {
      "bank_name": "M-Shwari",
      "transaction_count": 12,
      "total_inflow": 15000.0,
      "total_outflow": 8000.0,
      "net_flow": 7000.0
    }
  ]
}

## Frontend Guide

### Interface Overview

1. **Header Section**
   - Connection status indicator
   - Current date display

2. **Progress Section** (shown during analysis)
   - Progress bar with percentage
   - Animated status messages

3. **Results Table**
   - Color-coded results by category
   - Scrollable view of all analysis data

4. **Control Panel**
   - Action buttons
   - Loan scoring guide

### Button Functions

- **Upload PDF**: Select and analyze M-Pesa statement
- **Save Results**: Export analysis to text file
- **Clear Table**: Clear current results
- **Cancel**: Stop ongoing analysis
- **API Status**: Check backend connection

### Loan Scoring Guide

| Score Range | Interpretation         | Eligibility |
|-------------|------------------------|-------------|
| 0-30%       | Low risk (good client) | ✅ Yes      |
| 30-70%      | Moderate risk          | ✅ Yes      |
| 70-100%     | High risk              | ❌ No       |

## Deployment

### Backend Deployment

#### Option 1: Local Server
# Production mode (no reload)
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4


#### Option 2: Docker
dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]


#### Option 3: Cloud Platforms
- **Heroku**: Use Procfile with `web: uvicorn main:app --host=0.0.0.0 --port=$PORT`
- **AWS EC2**: Install dependencies and run with uvicorn
- **Google Cloud Run**: Containerized deployment

### Frontend Deployment

The frontend is a desktop application that can be distributed as:
- **Executable**: Use PyInstaller to create standalone executable
- **Source**: Distribute Python source code
- **Installer**: Create installers for Windows, macOS, Linux

#### Creating Executable
pip install pyinstaller
pyinstaller --onefile --windowed main.py

## Troubleshooting

### Common Issues

1. **API Connection Failed**
   - Ensure backend server is running
   - Check firewall settings
   - Verify API_BASE_URL in frontend config

2. **PDF Processing Errors**
   - Ensure PDF is a valid M-Pesa statement
   - Check if PDF is password protected
   - Verify PDF is not corrupted

3. **MongoDB Connection Issues**
   - Check MongoDB service is running
   - Verify connection string in .env file
   - Ensure network access to MongoDB

4. **ML Model Loading Failed**
   - Check credit_model.joblib and feature_columns.json exist
   - Verify file permissions
   - Check model compatibility with scikit-learn version

### Logs and Debugging

**Backend Logs:**
- Check console output for detailed error messages
- Enable debug mode with `--log-level debug`

**Frontend Logs:**
- Logs are displayed in the console
- Check connection status in the header

## Development

### Adding New Features

#### Backend Development
1. Add new routes in `routers/` directory
2. Implement business logic in `services/`
3. Update database models in `database/models.py`
4. Test with API documentation

#### Frontend Development
1. Create new components in `components/`
2. Add services in `services/`
3. Update configuration in `config/`
4. Test GUI functionality

### Testing

#### Backend Testing
# Install test dependencies
pip install pytest httpx

# Run tests
pytest tests/


#### Frontend Testing
- Manual testing of GUI components
- API integration testing
- PDF processing validation

### Code Structure Guidelines

- Follow PEP 8 style guide
- Use type hints for better code clarity
- Document functions with docstrings
- Write unit tests for new functionality
- Use meaningful variable and function names

## ML Model Information

### Features Used
- Monthly inflow/outflow amounts
- Transaction patterns
- Mobile loan activity
- Betting transactions
- Repayment history
- Spending categories

### Model Training
The model is trained on historical loan data using Random Forest classifier. To retrain:

1. Prepare training data with features and labels
2. Use `train_model.py` script (if available)
3. Validate model performance
4. Deploy new model files


## License

This project is licensed under the MIT License - see the LICENSE file for details.


---

**Note**: This system is designed for financial analysis and should be used in compliance with relevant regulations and data privacy laws. Always ensure proper authorization before analyzing customer financial data.