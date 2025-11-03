from pymongo import MongoClient
from config.settings import MONGODB_URI, DB_NAME

class DatabaseManager:
    def __init__(self):
        self.client = None
        self.db_connected = False
    
    def get_client(self):
        if self.client is None:
            try:
                self.client = MongoClient(
                    MONGODB_URI,
                    maxPoolSize=200,
                    minPoolSize=50,
                    
                )
                self.client.admin.command('ping')
                self.db_connected = True
                print("✓ MongoDB connection pool established")
            except Exception as e:
                print(f"MongoDB connection failed: {e}")
                self.client = None
        return self.client
    
    def get_database(self):
        client = self.get_client()
        return client[DB_NAME] if client else None
    
    def check_connection(self):
        try:
            client = self.get_client()
            if client:
                client.admin.command('ping')
                return True
            return False
        except Exception:
            return False

# Global instance
db_manager = DatabaseManager()