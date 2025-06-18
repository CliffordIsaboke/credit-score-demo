def extract_features(df):
    inflow = df[df['paid_in'] > 0]['paid_in'].sum()
    outflow = df[df['withdrawn'] > 0]['withdrawn'].sum()
    net_flow = inflow - outflow

    repayments = df['details'].str.contains("repay|tingg|eclof|loan|m-kopa", case=False, na=False).sum()
    repayment_ratio = repayments / inflow if inflow > 0 else 0

    balance_volatility = df['balance'].std() if 'balance' in df.columns else 0
    avg_transaction = df[df['paid_in'] > 0]['paid_in'].mean() or 0
    transaction_count = len(df)

    return {
        'monthly_inflow': inflow,
        'monthly_outflow': outflow,
        'net_cash_flow': net_flow,
        'repayments': repayments,
        'repayment_ratio': repayment_ratio,
        'balance_volatility': balance_volatility,
        'avg_transaction_amount': avg_transaction,
        'transaction_count': transaction_count
    }
