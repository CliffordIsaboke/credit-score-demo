import shap
import pandas as pd
from joblib import load
from feature_engineering import extract_features

model = load("credit_model.joblib")

# Load some sample data for explanation
df = pd.read_csv("mpesa_synthetic_data.csv")

features = extract_features(df)
X = pd.DataFrame([features])

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

shap.summary_plot(shap_values, X, show=True)
