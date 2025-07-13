import pandas as pd

df = pd.read_csv("data/monthly_summary.csv")

print("➡️ Monthly summary loaded:")
print(df.head())

persona_map = {
    "Family Support": "The Provider",
    "Car & Transport": "The Hustler",
    "Food & Drinks": "The Comfort Seeker",
    "Subscriptions & Entertainment": "The Escapist",
    "Health": "The Caretaker",
    "Utilities & Bills": "The Responsible One",
    "Bank Charges": "The Taxed-Out",
    "Personal & Gifts": "The Giver",
    "Transfers & P2P": "The Middleman",
    "Unknown": "The Enigma",
    "Uncategorized": "The Wildcard"
}

# Drop rows with zero debit
df = df[df["total_debit"] > 0]

top_per_month = (
    df.groupby("month")
    .apply(lambda x: x.loc[x["total_debit"].idxmax()])
    .reset_index(drop=True)
)

top_per_month["persona"] = top_per_month["category"].map(persona_map)
top_per_month.to_csv("data/monthly_personas.csv", index=False)

print("✅ Personas generated:")
print(top_per_month)
