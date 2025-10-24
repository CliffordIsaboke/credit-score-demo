import os
from dotenv import load_dotenv

load_dotenv()

# Performance Configuration
MAX_CONCURRENT_USERS = 100
UVICORN_WORKERS = 4
THREAD_POOL_WORKERS = 100
PROCESS_POOL_WORKERS = 8

# MongoDB Configuration
MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
RESULTS_COLLECTION = os.getenv("RESULTS_COLLECTION")
CLIENTS_COLLECTION = os.getenv("CLIENTS_COLLECTION")

# Model Configuration
MODEL_PATH = "credit_model.joblib"
FEATURES_PATH = "feature_columns.json"