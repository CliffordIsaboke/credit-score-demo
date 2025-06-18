import pdfplumber
import pandas as pd

def parse_mpesa_tables(pdf_path):
    all_data = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                if not table or len(table[0]) < 5:
                    continue
                headers = table[0]
                for row in table[1:]:
                    if len(row) != len(headers):
                        continue
                    row_dict = dict(zip(headers, row))
                    all_data.append(row_dict)

    df = pd.DataFrame(all_data)

    if df.empty:
        return df

    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    for col in ['paid_in', 'withdrawn', 'balance']:
        if col in df.columns:
            df[col] = (
                df[col].replace({'-': '0', '': '0', None: '0'})
                .fillna('0')
                .astype(str)
                .str.replace(',', '', regex=False)
                .astype(float)
            )

    if 'completion_time' in df.columns:
        df['completion_time'] = pd.to_datetime(df['completion_time'], errors='coerce')

    return df
