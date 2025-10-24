import os
import json
import numpy as np
import pandas as pd
from joblib import load
from sklearn.ensemble import RandomForestClassifier

class MLService:
    def __init__(self):
        self.model = None
        self.feature_columns = []
        self.model_loaded = False
    
    def load_model(self):
        """Load ML model with fallback"""
        try:
            if os.path.exists("credit_model.joblib") and os.path.exists("feature_columns.json"):
                self.model = load("credit_model.joblib")
                with open("feature_columns.json", "r") as f:
                    self.feature_columns = sorted(json.load(f))
                
                # Test model
                dummy_features = {col: 0 for col in self.feature_columns}
                X_test = pd.DataFrame([dummy_features])[self.feature_columns]
                self.model.predict_proba(X_test)
                self.model_loaded = True
                print("✅ Machine learning model loaded successfully")
            else:
                self._create_fallback_model()
        except Exception as e:
            print(f"❌ Could not load trained model: {e}")
            self._create_fallback_model()
    
    def _create_fallback_model(self):
        """Create fallback dummy model"""
        from sklearn.ensemble import RandomForestClassifier
        
        self.feature_columns = [
            'avg_transaction_amount', 'balance_volatility', 'betting_earnings',
            # ... your feature columns
        ]
        self.feature_columns = sorted(self.feature_columns)
        
        np.random.seed(42)
        X_dummy = np.random.rand(100, len(self.feature_columns))
        y_dummy = np.random.randint(0, 2, 100)
        
        self.model = RandomForestClassifier(n_estimators=10, random_state=42)
        self.model.fit(X_dummy, y_dummy)
        self.model_loaded = True
        print("✅ Fallback dummy model created and trained")
    
    def predict(self, features):
        """Make prediction using loaded model"""
        if not self.model_loaded:
            raise ValueError("Model not loaded")
        
        model_features = {}
        for col in self.feature_columns:
            model_features[col] = features.get(col, 0)
        
        X = pd.DataFrame([model_features])[self.feature_columns]
        return self.model.predict_proba(X)[0][1]

# Global instance
ml_service = MLService()