import pdfplumber
import pandas as pd
import re

pdf_path = "data/5703007018 - Henry Dibie’s Bank statement.pdf"
csv_path = "data/transactions.csv"

transactions = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        table = page.extract_table()
        if not table:
            continue

        for row in table:
            # Skip headers or malformed rows
            if not row or not isinstance(row[0], str) or "date" in row[0].lower():
                continue

            # Try extracting transaction info from expected structure
            # Fallback to padding if needed
            clean_row = row + [None] * (30 - len(row))  # pad to 30

            txn_date = clean_row[0] or clean_row[3]
            val_date = clean_row[3] or clean_row[0]
            remarks = next((cell for cell in clean_row[5:15] if cell), "")
            debit = next((cell for cell in clean_row if re.match(r"^\d{1,3}(,\d{3})*(\.\d{2})?$", str(cell))), "0")
            credit = "0"
            balance = None

            # Try parsing debit, credit, and balance correctly
            try:
                amount = float(debit.replace(",", ""))
                if "charge" in str(remarks).lower() or "to" in str(remarks).lower():
                    debit_val = amount
                    credit_val = 0.0
                else:
                    credit_val = amount
                    debit_val = 0.0
            except:
                debit_val = 0.0
                credit_val = 0.0

            transactions.append({
                "txn_date": txn_date.strip() if txn_date else "",
                "val_date": val_date.strip() if val_date else "",
                "remarks": re.sub(r"\s+", " ", str(remarks)).strip(),
                "debit": debit_val,
                "credit": credit_val,
                "balance": balance
            })

df = pd.DataFrame(transactions)
df.to_csv(csv_path, index=False)
print(f"✅ Extracted {len(df)} transactions to {csv_path}")
