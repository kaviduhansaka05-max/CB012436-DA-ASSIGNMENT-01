import pandas as pd
import matplotlib.pyplot as plt
import os

# Create folders
os.makedirs("../outputs/graphs", exist_ok=True)
os.makedirs("../outputs/tables", exist_ok=True)

# Load dataset
audience_df = pd.read_excel(r"../data/Company_X_Audience.xlsx")

# Create Engagement_Value metric
audience_df["Engagement_Value"] = (
    audience_df["Merchandise_Spend"] + audience_df["Drink_Spend"]
) / audience_df["Ticket_Price"]

# Summary statistics
engagement_summary = audience_df["Engagement_Value"].describe().round(2)

print("=" * 90)
print("ENGAGEMENT VALUE SUMMARY")
print("=" * 90)
print(engagement_summary)

# Average Engagement_Value by Seating Region
region_summary = audience_df.groupby("Seating_Region")["Engagement_Value"].agg(
    Count="count",
    Mean="mean",
    Median="median",
    Std_Dev="std",
    Min="min",
    Max="max"
).round(2)

print("\n" + "=" * 90)
print("ENGAGEMENT VALUE BY SEATING REGION")
print("=" * 90)
print(region_summary)

# Save table
region_summary.to_csv(r"../outputs/tables/engagement_value_by_region.csv")

# Histogram of Engagement Value
plt.figure(figsize=(10, 6))
plt.hist(audience_df["Engagement_Value"].dropna(), bins=20, edgecolor="black")
plt.title("Distribution of Engagement Value")
plt.xlabel("Engagement Value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(r"../outputs/graphs/engagement_value_distribution.png", dpi=300)
plt.show()

# Mean Engagement Value by Seating Region
plt.figure(figsize=(9, 6))
region_summary["Mean"].plot(kind="bar", edgecolor="black")
plt.title("Average Engagement Value by Seating Region")
plt.xlabel("Seating Region")
plt.ylabel("Average Engagement Value")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(r"../outputs/graphs/engagement_value_by_region.png", dpi=300)
plt.show()

# Scatter plot: Ticket Price vs Engagement Value
plt.figure(figsize=(10, 6))
plt.scatter(audience_df["Ticket_Price"], audience_df["Engagement_Value"], alpha=0.6)
plt.title("Ticket Price vs Engagement Value")
plt.xlabel("Ticket Price")
plt.ylabel("Engagement Value")
plt.tight_layout()
plt.savefig(r"../outputs/graphs/ticket_price_vs_engagement_value.png", dpi=300)
plt.show()