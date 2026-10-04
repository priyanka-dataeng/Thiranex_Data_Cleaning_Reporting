import pandas as pd
import matplotlib.pyplot as plt

print("DATA CLEANING & REPORTING AUTOMATION")
print("------------------------------------")

# Load dataset
df = pd.read_csv("Project4_Messy_Sales_Data.csv")

print("\nOriginal Dataset Shape:", df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())
df["Region"] = df["Region"].fillna("Unknown")

# Standardize inconsistent text
df["Product"] = df["Product"].str.strip().str.title()
df["Region"] = df["Region"].str.strip().str.title()

# Create Sales column
df["Sales"] = df["Quantity"] * df["Unit_Price"]

# Save cleaned dataset
df.to_csv("Cleaned_Sales_Data.csv", index=False)

# Generate summary report
summary = df.groupby("Category")["Sales"].sum().reset_index()
summary.to_csv("Sales_Summary_Report.csv", index=False)

print("\nCleaned Dataset Shape:", df.shape)
print("\nSales Summary:")
print(summary)

# Generate visualization
summary.plot(
    x="Category",
    y="Sales",
    kind="bar",
    legend=False,
    title="Total Sales by Category"
)

plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("Sales_Report_Chart.png")
plt.close()

print("\nCleaned_Sales_Data.csv created")
print("Sales_Summary_Report.csv created")
print("Sales_Report_Chart.png created")

print("\nDATA CLEANING & REPORTING COMPLETED")