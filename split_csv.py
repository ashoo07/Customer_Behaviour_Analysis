import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

# Read the original single file
df = pd.read_csv("customer_shopping_behavior.csv", encoding="utf-8-sig")

# 1) Customers: one row per customer
customers = df[["Customer ID", "Age", "Gender", "Location",
                "Subscription Status", "Previous Purchases",
                "Frequency of Purchases"]]

# 2) Products: one row per unique item
products = (df[["Item Purchased", "Category"]]
            .drop_duplicates()
            .sort_values("Item Purchased"))

# 3) Purchases: one row per purchase (links customers to products)
purchases = df[["Customer ID", "Item Purchased", "Purchase Amount (USD)",
                "Review Rating", "Size", "Color", "Season", "Shipping Type",
                "Discount Applied", "Promo Code Used", "Payment Method"]]

customers.to_csv(RAW_DIR / "customers.csv", index=False)
products.to_csv(RAW_DIR / "products.csv", index=False)
purchases.to_csv(RAW_DIR / "purchases.csv", index=False)

print("customers:", len(customers), "rows")
print("products :", len(products), "rows")
print("purchases:", len(purchases), "rows")