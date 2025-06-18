import pandas as pd
import random
from sklearn.ensemble import RandomForestClassifier
from joblib import dump
from feature_engineering import extract_features

df = pd.read_csv("sample_mpesa.csv")  # renamed for clarity

samples = []
for _ in range(100):
    inflow = random.randint(1000, 20000)
    outflow = random.randint(500, inflow)
    repayments = random.randint(0, 5)
    repayment_ratio = repayments / inflow if inflow > 0 else 0
    balance_volatility = random.uniform(0, 1000)
    avg_transaction = inflow / random.randint(10, 50)
    transaction_count = random.randint(10, 150)

    label = 1 if inflow < 3000 or repayments == 0 else 0

    samples.append({
        'monthly_inflow': inflow,
        'monthly_outflow': outflow,
        'net_cash_flow': inflow - outflow,
        'repayments': repayments,
        'repayment_ratio': repayment_ratio,
        'balance_volatility': balance_volatility,
        'avg_transaction_amount': avg_transaction,
        'transaction_count': transaction_count,
        'loan_defaulted': label
    })

train_df = pd.DataFrame(samples)
X = train_df.drop('loan_defaulted', axis=1)
y = train_df['loan_defaulted']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

dump(model, 'credit_model.joblib')
print("✅ Model trained and saved as credit_model.joblib")
