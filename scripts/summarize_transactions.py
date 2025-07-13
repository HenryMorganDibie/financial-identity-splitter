import pandas as pd
from pathlib import Path

df = pd.read_csv("data/transactions_categorized.csv")

# Step 1: Check original structure
print("✅ Loaded:", len(df), "rows")
print("🔍 Sample remarks:")
print(df["remarks"].dropna().head(5))

# Step 2: Convert txn_date
df["txn_date"] = pd.to_datetime(df["txn_date"], format="%d-%b-%Y", errors="coerce")
print("\n✅ txn_date after parsing:")
print(df["txn_date"].dropna().head())

# Step 3: Fix debit/credit columns
df["debit"] = pd.to_numeric(df["debit"], errors="coerce").fillna(0)
df["credit"] = pd.to_numeric(df["credit"], errors="coerce").fillna(0)

# Step 4: Clean out invalids
df = df.dropna(subset=["txn_date", "remarks"])
df = df[df["debit"] > 0]

print("\n✅ Filtered:", len(df), "rows with valid debit & date")

# Step 5: Extract month
df["month"] = df["txn_date"].dt.to_period("M").astype(str)

# Step 6: Summarize
summary = (
    df.groupby(["month", "category"])
    .agg(total_debit=("debit", "sum"), total_credit=("credit", "sum"))
    .reset_index()
    .sort_values(by=["month", "total_debit"], ascending=[True, False])
)

# Step 7: Save
summary.to_csv("data/monthly_summary.csv", index=False)
print("\n✅ Cleaned & saved summary with", len(summary), "rows.")
