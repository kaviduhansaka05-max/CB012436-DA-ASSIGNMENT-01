import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Load dataset
audience_df = pd.read_excel(r"../data/Company_X_Audience.xlsx")

# Filter VIP and Economy groups
vip_scores = audience_df[audience_df["Seating_Region"] == "VIP"]["Satisfaction_Score"]
economy_scores = audience_df[audience_df["Seating_Region"] == "Economy"]["Satisfaction_Score"]

# Summary statistics
summary = pd.DataFrame({
    "Group": ["VIP", "Economy"],
    "Count": [vip_scores.count(), economy_scores.count()],
    "Mean": [vip_scores.mean(), economy_scores.mean()],
    "Median": [vip_scores.median(), economy_scores.median()],
    "Std Dev": [vip_scores.std(), economy_scores.std()],
    "Min": [vip_scores.min(), economy_scores.min()],
    "Max": [vip_scores.max(), economy_scores.max()]
}).round(2)

print("=" * 90)
print("VIP VS ECONOMY - SATISFACTION SCORE SUMMARY")
print("=" * 90)
print(summary.to_string(index=False))

# Independent t-test
t_stat, p_two_tailed = ttest_ind(vip_scores, economy_scores, equal_var=False)

# Convert to one-tailed p-value for VIP > Economy
if vip_scores.mean() > economy_scores.mean():
    p_one_tailed = p_two_tailed / 2
else:
    p_one_tailed = 1 - (p_two_tailed / 2)

print("\n" + "=" * 90)
print("T-TEST RESULTS")
print("=" * 90)
print(f"T-statistic: {t_stat:.4f}")
print(f"One-tailed p-value (VIP > Economy): {p_one_tailed:.4f}")

# Save summary table
summary.to_csv(r"../outputs/tables/vip_vs_economy_satisfaction_summary.csv", index=False)

# Histogram
plt.figure(figsize=(10, 6))
plt.hist(vip_scores, bins=10, alpha=0.6, label="VIP", edgecolor="black")
plt.hist(economy_scores, bins=10, alpha=0.6, label="Economy", edgecolor="black")
plt.title("Histogram of Satisfaction Score: VIP vs Economy")
plt.xlabel("Satisfaction Score")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.savefig(r"../outputs/graphs/vip_vs_economy_histogram.png")
plt.show()

# Mean bar chart
plt.figure(figsize=(8, 6))
plt.bar(summary["Group"], summary["Mean"], edgecolor="black")
plt.title("Mean Satisfaction Score: VIP vs Economy")
plt.xlabel("Seating Region")
plt.ylabel("Mean Satisfaction Score")
plt.tight_layout()
plt.savefig(r"../outputs/graphs/vip_vs_economy_mean_bar_chart.png")
plt.show()