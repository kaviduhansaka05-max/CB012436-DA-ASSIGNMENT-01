import pandas as pd
import matplotlib.pyplot as plt
import os

# =========================================================
# PART B (g) - THREE ADDITIONAL KEY VISUALIZATIONS
# =========================================================

# Create output folders
os.makedirs(r"../outputs/graphs", exist_ok=True)
os.makedirs(r"../outputs/tables", exist_ok=True)

# Load datasets
audience_df = pd.read_excel(r"../data/Company_X_Audience.xlsx")
show_df = pd.read_excel(r"../data/Company_X_ShowData.xlsx")

print("=" * 100)
print("PART B (g) - THREE ADDITIONAL KEY VISUALIZATIONS FOR BUSINESS DECISION MAKING")
print("=" * 100)

# =========================================================
# VISUALIZATION 1
# Average Revenue by Region and Day Type
# =========================================================
print("\n" + "=" * 100)
print("VISUALIZATION 1: AVERAGE REVENUE BY REGION AND DAY TYPE")
print("=" * 100)

revenue_region_day = show_df.groupby(["Region", "Day_Type"])["Revenue"].mean().unstack()
revenue_region_day = revenue_region_day.round(2)

print("\nAverage Revenue by Region and Day Type:")
print(revenue_region_day)

# Save table
revenue_region_day.to_csv(r"../outputs/tables/g1_revenue_by_region_daytype.csv")

# Plot
revenue_region_day.plot(kind="bar", figsize=(10, 6), edgecolor="black")
plt.title("Average Revenue by Region and Day Type")
plt.xlabel("Region")
plt.ylabel("Average Revenue")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(r"../outputs/graphs/g1_revenue_by_region_daytype.png")
plt.show()

# =========================================================
# VISUALIZATION 2
# Average Revenue by Weather Score
# =========================================================
print("\n" + "=" * 100)
print("VISUALIZATION 2: AVERAGE REVENUE BY WEATHER SCORE")
print("=" * 100)

# Round weather scores into whole-number groups
show_df["Weather_Group"] = show_df["Weather_Score"].round().astype(int)

weather_summary = show_df.groupby("Weather_Group")["Revenue"].agg(["count", "mean", "min", "max"])
weather_summary = weather_summary.sort_index().round(2)

print("\nAverage Revenue by Weather Score:")
print(weather_summary)

# Save table
weather_summary.to_csv(r"../outputs/tables/g2_average_revenue_by_weather_score.csv")

# Plot bar chart using mean revenue
plt.figure(figsize=(10, 6))
plt.bar(weather_summary.index.astype(str), weather_summary["mean"], edgecolor="black")
plt.title("Average Revenue by Weather Score")
plt.xlabel("Weather Score")
plt.ylabel("Average Revenue")
plt.tight_layout()
plt.savefig(r"../outputs/graphs/g2_average_revenue_by_weather_score.png")
plt.show()

# =========================================================
# VISUALIZATION 3
# Average Revenue by Guest Performance
# =========================================================
print("\n" + "=" * 100)
print("VISUALIZATION 3: AVERAGE REVENUE BY GUEST PERFORMANCE")
print("=" * 100)

guest_revenue = show_df.groupby("Guest_Performance")["Revenue"].agg(["count", "mean", "min", "max"]).round(2)

print("\nAverage Revenue by Guest Performance:")
print(guest_revenue)

# Save table
guest_revenue.to_csv(r"../outputs/tables/g3_average_revenue_by_guest_performance.csv")

# Plot
plt.figure(figsize=(8, 6))
plt.bar(guest_revenue.index.astype(str), guest_revenue["mean"], edgecolor="black")
plt.title("Average Revenue by Guest Performance")
plt.xlabel("Guest Performance")
plt.ylabel("Average Revenue")
plt.tight_layout()
plt.savefig(r"../outputs/graphs/g3_average_revenue_by_guest_performance.png")
plt.show()
# =========================================================
# SUMMARY OF SAVED OUTPUTS
# =========================================================
print("\n" + "=" * 100)
print("SUMMARY OF SAVED OUTPUTS")
print("=" * 100)
print("Graphs saved:")
print("1. ../outputs/graphs/g1_revenue_by_region_daytype.png")
print("2. ../outputs/graphs/g2_average_revenue_by_weather_score.png")
print("3. ../outputs/graphs/g3_repeat_visit_rate_by_seating_region.png")

print("\nTables saved:")
print("1. ../outputs/tables/g1_revenue_by_region_daytype.csv")
print("2. ../outputs/tables/g2_average_revenue_by_weather_score.csv")
print("3. ../outputs/tables/g3_repeat_visit_rate_by_seating_region.csv")

print("\nPart B (g) visualizations completed successfully.")