import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
show_df = pd.read_excel(r"../data/Company_X_ShowData.xlsx")

# Convert date column to datetime
show_df["Show_Date"] = pd.to_datetime(show_df["Show_Date"])

# Create month column
show_df["Month"] = show_df["Show_Date"].dt.to_period("M").astype(str)

# Group total revenue by month and region
monthly_revenue = show_df.groupby(["Month", "Region"])["Revenue"].sum().reset_index()

# Create pivot table
pivot_df = monthly_revenue.pivot(index="Month", columns="Region", values="Revenue")

# Show pivot table before filling missing values
print("=" * 100)
print("MONTHLY TOTAL TICKET REVENUE BY REGION (BEFORE FILLING MISSING VALUES)")
print("=" * 100)
print(pivot_df.round(2))

print("\nMissing values by region before filling:")
print(pivot_df.isna().sum())

# Fill missing month-region combinations with 0
pivot_df = pivot_df.fillna(0)

# Show pivot table after filling missing values
print("\n" + "=" * 100)
print("MONTHLY TOTAL TICKET REVENUE BY REGION (AFTER FILLING MISSING VALUES WITH 0)")
print("=" * 100)
print(pivot_df.round(2))

# Save summary table
pivot_df.round(2).to_csv(r"../outputs/tables/monthly_revenue_by_region.csv")

# Plot trend chart
plt.figure(figsize=(12, 6))

for region in pivot_df.columns:
    plt.plot(pivot_df.index, pivot_df[region], marker="o", linewidth=2, label=region)

plt.title("Total Ticket Revenue Over Time by Region")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.legend(title="Region")
plt.tight_layout()

# Save graph
plt.savefig(r"../outputs/graphs/revenue_trend_by_region.png")
plt.show()

print("\nTrend chart and monthly summary table saved successfully.")