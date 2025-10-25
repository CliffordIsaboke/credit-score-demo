
# Loan Analysis System

A comprehensive **full-stack application** for analyzing M-Pesa statements and calculating **loan eligibility scores** using **machine learning**.

---

## Overview

The **Loan Scoring System** consists of:

* **Backend API** – FastAPI-based REST API for PDF processing and ML scoring
* **Frontend GUI** – CustomTkinter desktop app for user interaction
* **Machine Learning** – Random Forest model for credit risk assessment
* **Database** – MongoDB for storing analysis results and client data

---

### Key Capabilities

* Analyze M-Pesa statement PDFs
* Machine learning–powered credit scoring
* Detect banking and mobile loan transactions
* Identify spending patterns and financial behavior
* Calculate financial metrics and eligibility
* Save and manage analysis results

---

## Features

### Backend Features

* **High Performance** – Supports 100+ concurrent users
* **PDF Processing** – Advanced M-Pesa statement parsing
* **ML Integration** – Pre-trained credit scoring model
* **Bank Detection** – 100+ Kenyan banks supported
* **Transaction Analysis** – Categorizes spending patterns
* **RESTful API** – Comprehensive API endpoints
* **MongoDB Integration** – Scalable data storage
* **Async Processing** – Non-blocking PDF handling

### Frontend Features

* **Modern GUI** – CustomTkinter interface
* **Real-Time Progress** – Animated progress indicators
* **Password Support** – Encrypted PDF handling
* **Results Export** – Save analysis to text files
* **Connection Monitoring** – Live API status updates
* **Responsive Design** – Adapts to various screen sizes

---

## Project Structure

### Backend (`loan_scoring_api/`)

```
loan_scoring_api/
├── main.py              # FastAPI app entry point
├── config/              # Configuration settings
├── database/            # MongoDB models & connection
├── services/            # Business logic
├── routers/             # API routes
└── utils/               # Utility functions
```

### Frontend (`loan_scoring_frontend/`)

```
loan_scoring_frontend/
├── main.py              # GUI entry point
├── config/              # App settings and styling
├── components/          # UI components
├── services/            # API clients & file handling
└── utils/               # Helper functions
```

---

## Installation

### Prerequisites

* Python 3.8+
* MongoDB (local or cloud)
* Required Python packages

---

### Backend Setup

```bash
# 1. Clone repository
git clone https://github.com/CliffordIsaboke/mpesa-credit-score-demo.git
cd loan_scoring_api

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
# (edit example.env with MongoDB details)

# 5. Start MongoDB (if local)
mongod --dbpath /path/to/data
```

---

### Frontend Setup

```bash
# 1. Navigate to frontend directory
cd loan_scoring_frontend

# 2. Install dependencies
pip install -r requirements.txt
```

---

## Configuration

### Backend (`.env`)

```bash
MONGODB_URI=mongodb://localhost:27017
DB_NAME=loan_scoring
COLLECTION_NAME=system_config
RESULTS_COLLECTION=analysis_results
CLIENTS_COLLECTION=clients
```

**Optional (Cloud MongoDB):**

```bash
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/
```

### Frontend (`config/settings.py`)

```python
# Local development
API_BASE_URL = "http://127.0.0.1:8000"

# Production
# API_BASE_URL = "http://your-server-ip:8000"
```

---

## Usage

### Starting the Backend

```bash
cd loan_scoring_api
python main.py
# or
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Visit: **[http://localhost:8000](http://localhost:8000)** to view API docs.

### Starting the Frontend

```bash
cd loan_scoring_frontend
python main.py
```

**Using the App:**

* Click **Upload PDF**
* Enter loan amount
* Provide password (if required)
* View analysis results and score

---

## API Documentation

### Base URL

```
http://localhost:8000
```

### Endpoints

#### Analysis

* `POST /analyze` – Analyze PDF and calculate score
* `GET /status` – Check API health
* `GET /` – API overview

#### Banking

* `GET /banks` – List supported banks
* `POST /analyze-bank` – Analyze bank transactions

---

### Example Requests

**Check API status**

```bash
curl http://localhost:8000/status
```

**Analyze a PDF**

```bash
curl -X POST -F "file=@statement.pdf" -F "loan_amount=50000" http://localhost:8000/analyze
```

---

### Example Response

```json
{
  "success": true,
  "result_id": "unique_id",
  "results": [
    {"metric": "Client Name", "value": "John Doe", "category": "basic_info"}
  ],
  "client_info": {"name": "John Doe", "phone": "254712345678"},
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
```

---

## Frontend Guide

### Interface Overview

1. **Header** – Connection status, date display
2. **Progress Section** – Animated progress bar
3. **Results Table** – Color-coded analysis results
4. **Control Panel** – Action buttons

### Button Functions

| Button           | Function                     |
| ---------------- | ---------------------------- |
| **Upload PDF**   | Select and analyze statement |
| **Save Results** | Export analysis to file      |
| **Clear Table**  | Clear displayed data         |
| **Cancel**       | Stop current analysis        |
| **API Status**   | Check backend connection     |

### Loan Scoring Guide

| Score Range | Interpretation | Eligibility |
| ----------- | -------------- | ----------- |
| 0–30%       | Low risk       | ✅ Yes       |
| 30–70%      | Moderate risk  | ✅ Yes       |
| 70–100%     | High risk      | ❌ No        |

---

## Deployment

### Backend

**Local (Production Mode)**

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

**Dockerfile**

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
```

**Cloud Options:**

* Heroku
* AWS EC2
* Google Cloud Run

### Frontend Distribution

* **Executable**: via PyInstaller
* **Source Code**: share Python scripts
* **Installer**: create for Windows/macOS/Linux

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

---

## Troubleshooting

| Issue                 | Possible Fix                        |
| --------------------- | ----------------------------------- |
| API Connection Failed | Check server and `API_BASE_URL`     |
| PDF Error             | Ensure valid M-Pesa PDF             |
| MongoDB Error         | Verify `.env` connection            |
| Model Load Failed     | Ensure `credit_model.joblib` exists |

---

## Development

### Adding Features

**Backend**

1. Add routes → `routers/`
2. Implement logic → `services/`
3. Update models → `database/models.py`

**Frontend**

1. Add components → `components/`
2. Add API logic → `services/`
3. Update config → `config/`

---

### Testing

**Backend**

```bash
pip install pytest httpx
pytest tests/
```

**Frontend**

* Manual GUI testing
* API integration validation
* PDF input verification

---

## ML Model

### Features

* Monthly inflows/outflows
* Mobile loan activity
* Betting transactions
* Spending patterns
* Repayment history

### Training

1. Prepare labeled dataset
2. Train Random Forest model
3. Validate and deploy

---

## License

Licensed under the **MIT License**.
See the [LICENSE](./LICENSE) file for details.

---

**Note:** Use this system responsibly and in compliance with financial regulations and data privacy laws.








