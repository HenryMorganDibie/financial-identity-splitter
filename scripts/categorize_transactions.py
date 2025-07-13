import pandas as pd
import re

# Load the transactions
df = pd.read_csv("data/transactions.csv")

# Define categories and keywords
category_keywords = {
    "Food & Drinks": ["shawarma", "suya", "milk", "bread", "pizza", "biscuit", "cake", "egg", "indomie", "drink", "ice cream"],
    "Subscriptions & Entertainment": ["netflix", "icloud", "tv", "console", "spotify"],
    "Transfers & P2P": ["palmpay", "opay", "kuda", "uba", "wema", "access bank", "sterling", "keystone", "moniepoint", "uba"],
    "Car & Transport": ["fuel", "tyre", "mechanic", "radiator", "panel", "painting", "car wash", "gear", "bumper"],
    "Family Support": ["mum", "dad", "harry", "victoria", "morgan", "birthday", "allowance"],
    "Utilities & Bills": ["light", "quickteller", "bills", "internet", "payment", "airtime", "data", "electricity", "levy"],
    "Health": ["hospital", "medication", "antenatal", "pharmacy", "health"],
    "Personal & Gifts": ["gift", "clothes", "shirt", "shoes", "necklace", "haircut", "plumber", "sewing"],
    "Bank Charges": ["charge", "fee", "levy", "vat", "sms", "maintenance"],
    "Unknown": []
}

def categorize(remark):
    if not isinstance(remark, str):
        return "Uncategorized"
    
    remark = remark.lower()
    for category, keywords in category_keywords.items():
        if any(re.search(rf"\b{k}\b", remark) for k in keywords):
            return category
    return "Uncategorized"

# Apply categorization
df["category"] = df["remarks"].apply(categorize)

# Save updated CSV
df.to_csv("data/transactions_categorized.csv", index=False)
print("✅ Transactions categorized and saved to data/transactions_categorized.csv")
