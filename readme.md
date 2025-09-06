# M-Pesa Behavioral Credit Scoring Demo

A demo project showcasing the use of data science and machine learning to build a behavioral credit scoring system using raw M-Pesa statements. 
---

## Project Overview

This solution simulates how financial institutions can assess a borrower’s creditworthiness using transactional behavior instead of traditional credit history. Using realistic M-Pesa-style statement data (in PDF or CSV), the pipeline includes:

- PDF parsing and normalization of transaction data
- Behavioral feature engineering (repayment patterns, volatility, etc.)
- Classification model training and evaluation (Random Forest, XGBoost)
- SHAP explainability for ethical AI
- A simple dashboard for user interaction

---

## Repository Structure

| File/Folder                       | Purpose                                                               |
| --------------------------------- | --------------------------------------------------------------------- |
| `mpesa_synthetic_data.csv`        | A fake (but realistic) dataset to demonstrate the pipeline            |
| `parse_mpesa.py`                  | Code to clean and normalize raw M-Pesa data                           |
| `feature_engineering.py`          | Code for creating behavioral features                                 |
| `train_model.py`                  | Model training (XGBoost, Random Forest, etc.)                         |
| `credit_score_algorithm.py`       | Custom logic for scoring based on behavior                            |
| `model_performance_report.pdf`    | PDF summary of model metrics (accuracy, ROC, etc.)                    |
| `shap_plot_demo.py`               | SHAP explanation code                                                 |
| `SHAP_Interpretation.png`         | SHAP image (used in your evidence)                                    |
| `credit_dashboard.py`             | Dashboard code (Tkinter or Streamlit)                                 |
| `dashboard_images.png`            | Screenshot of the dashboard running                                   |
| `requirements.txt`                | Python libraries needed                                               |
| `LICENSE`                         | MIT License                                                           |
| `README.md`                       | This file                                                             |

---

### Sample Data
This repository includes a synthetic M-Pesa dataset (`mpesa_synthetic_dataset.csv`) for demonstration purposes only. It mimics the structure of real transaction data but contains no actual user or financial records.


## Setup Instructions

### 1. Clone the repository

git clone https://github.com/cliffordisaboke/mpesa-credit-score-demo

cd mpesa-credit-score-demo

### 2. Set up a virtual environment
python3 -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Running the Project

- To parse an M-Pesa PDF statement:

python parse_mpesa.py: This will extract transactions and output a cleaned CSV file (mpesa_dataset.csv.)

- To train a model using simulated behavioral features:

python train_model.py: The trained model is saved as credit_model.joblib.

- To test explainability with SHAP:

python shap_plot_demo.py: This will generate a SHAP image: SHAP_Interpretation.png.

- To launch the dashboard:

python credit_dashboard.py

### 5. Key Features
- Real-world simulation of M-Pesa behavior
- Explainable AI (XAI) via SHAP plots
- Ethical scoring through repayment patterns, not only income
- Custom credit algorithm built using domain-informed heuristics
- Simple GUI for real-time credit score display

### 6. Sample Output
- Model Accuracy: 92% (XGBoost)
- SHAP Factors: Repayments, inflow volume, transaction count
- Dashboard Output: Score + Eligibility tag

## License
This project is licensed under the MIT License.

---




