import pandas as pd

df = pd.read_csv("data/transactions_categorized.csv")

print("🧾 Sample rows:")
print(df[["txn_date", "remarks", "debit", "category"]].head(10))

print("\n🔍 Debit column types:")
print(df["debit"].dtype)

print("\n💰 Total rows with positive debit:")
print((df["debit"] > 0).sum())
