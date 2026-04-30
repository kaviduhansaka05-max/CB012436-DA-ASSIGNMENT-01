import pandas as pd
import matplotlib.pyplot as plt
import os

# =========================================================
# PART A (f) - OUTLIER / ANOMALY ANALYSIS
# Merchandise_Spend  -> Upright Boxplot + Histogram
# Drink_Spend        -> Upright Boxplot + Histogram
# Satisfaction_Score -> Upright Boxplot
# =========================================================

# Create output folders
os.makedirs(r"../outputs/graphs", exist_ok=True)
os.makedirs(r"../outputs/tables", exist_ok=True)

# Load dataset
audience_df = pd.read_excel(r"../data/Company_X_Audience.xlsx")

# Variables to analyse
columns = ["Merchandise_Spend", "Drink_Spend", "Satisfaction_Score"]

print("=" * 90)
print("OUTLIER / ANOMALY ANALYSIS")
print("=" * 90)

# Store IQR summary results
iqr_results = []

for col in columns:
    print("\n" + "=" * 90)
    print(f"{col.upper()} ANALYSIS")
    print("=" * 90)

    # Top 10 highest values
    print(f"\nTop 10 highest values in {col}:")
    print(audience_df[[col]].sort_values(by=col, ascending=False).head(10))

    # IQR calculation
    Q1 = audience_df[col].quantile(0.25)
    Q3 = audience_df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = audience_df[
        (audience_df[col] < lower_bound) | (audience_df[col] > upper_bound)
    ][[col]]

    num_outliers = len(outliers)

    print(f"\nQ1: {Q1:.2f}")
    print(f"Q3: {Q3:.2f}")
    print(f"IQR: {IQR:.2f}")
    print(f"Lower Bound: {lower_bound:.2f}")
    print(f"Upper Bound: {upper_bound:.2f}")
    print(f"Number of Outliers: {num_outliers}")

    # Save results for summary table
    iqr_results.append({
        "Variable": col,
        "Q1": round(Q1, 2),
        "Q3": round(Q3, 2),
        "IQR": round(IQR, 2),
        "Lower_Bound": round(lower_bound, 2),
        "Upper_Bound": round(upper_bound, 2),
        "Number_of_Outliers": num_outliers
    })

    # Save outlier values
    outliers.to_csv(rf"../outputs/tables/{col.lower()}_outliers.csv", index=False)

# =========================================================
# FIGURE 1 - Merchandise_Spend (Upright Boxplot + Histogram)
# =========================================================
fig, axes = plt.subplots(
    2, 1, figsize=(8, 10),
    gridspec_kw={"height_ratios": [1, 2]}
)

# Upright boxplot
axes[0].boxplot(audience_df["Merchandise_Spend"], vert=True)
axes[0].set_title("Boxplot of Merchandise_Spend")
axes[0].set_ylabel("Merchandise_Spend")

# Histogram
counts, bins, patches = axes[1].hist(
    audience_df["Merchandise_Spend"],
    bins=10,
    edgecolor="black",
    linewidth=1.2
)
bin_centers = 0.5 * (bins[:-1] + bins[1:])
axes[1].plot(bin_centers, counts, marker="o")
axes[1].set_title("Histogram of Merchandise_Spend")
axes[1].set_xlabel("Merchandise_Spend")
axes[1].set_ylabel("Frequency")

plt.tight_layout()
plt.savefig(r"../outputs/graphs/figure1_merchandise_box_hist_upright.png")
plt.show()

# =========================================================
# FIGURE 2 - Drink_Spend (Upright Boxplot + Histogram)
# =========================================================
fig, axes = plt.subplots(
    2, 1, figsize=(8, 10),
    gridspec_kw={"height_ratios": [1, 2]}
)

# Upright boxplot
axes[0].boxplot(audience_df["Drink_Spend"], vert=True)
axes[0].set_title("Boxplot of Drink_Spend")
axes[0].set_ylabel("Drink_Spend")

# Histogram
counts, bins, patches = axes[1].hist(
    audience_df["Drink_Spend"],
    bins=10,
    edgecolor="black",
    linewidth=1.2
)
bin_centers = 0.5 * (bins[:-1] + bins[1:])
axes[1].plot(bin_centers, counts, marker="o")
axes[1].set_title("Histogram of Drink_Spend")
axes[1].set_xlabel("Drink_Spend")
axes[1].set_ylabel("Frequency")

plt.tight_layout()
plt.savefig(r"../outputs/graphs/figure2_drink_box_hist_upright.png")
plt.show()

# =========================================================
# FIGURE 3 - Satisfaction_Score (Upright Boxplot only)
# =========================================================
plt.figure(figsize=(8, 6))
plt.boxplot(audience_df["Satisfaction_Score"], vert=True)
plt.title("Boxplot of Satisfaction_Score")
plt.ylabel("Satisfaction_Score")
plt.tight_layout()
plt.savefig(r"../outputs/graphs/figure3_satisfaction_boxplot_upright.png")
plt.show()

# =========================================================
# Save IQR summary table
# =========================================================
iqr_summary_df = pd.DataFrame(iqr_results)

print("\n" + "=" * 90)
print("IQR OUTLIER SUMMARY TABLE")
print("=" * 90)
print(iqr_summary_df)

iqr_summary_df.to_csv(r"../outputs/tables/iqr_outlier_summary.csv", index=False)

print("\nAll graphs and tables saved successfully.")