import pandas as pd

# Load dataset
df = pd.read_csv("sales.csv")

# Display data
print(df)

# Total Sales
print("\nTotal Sales:", df["Sales"].sum())

# Total Profit
print("Total Profit:", df["Profit"].sum())

# Best Selling Product
best_product = df.loc[df["Sales"].idxmax(), "Product"]
print("Best Selling Product:", best_product)

# Category-wise Sales
print("\nCategory-wise Sales:")
print(df.groupby("Category")["Sales"].sum())