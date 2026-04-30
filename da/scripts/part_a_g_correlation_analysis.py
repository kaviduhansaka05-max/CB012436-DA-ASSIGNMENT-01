import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Create output folders
os.makedirs(r"../outputs/graphs", exist_ok=True)
os.makedirs(r"../outputs/tables", exist_ok=True)

# Load dataset
audience_df = pd.read_excel(r"../data/Company_X_Audience.xlsx")

# Select variables for correlation
corr_data = audience_df[["Ticket_Price", "Merchandise_Spend", "Drink_Spend", "Satisfaction_Score"]]

# Pearson correlation matrix
corr_matrix = corr_data.corr(method="pearson")

print("=" * 100)
print("EXACT PEARSON CORRELATION MATRIX")
print("=" * 100)
print(corr_matrix)

# Save correlation table
corr_matrix.to_csv(r"../outputs/tables/correlation_matrix_exact.csv")


# =========================================================
# 1. CORRELATION HEATMAP
# =========================================================
plt.figure(figsize=(8, 6))
plt.imshow(corr_matrix, cmap="coolwarm", interpolation="nearest")
plt.colorbar(label="Pearson r")

plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=45)
plt.yticks(range(len(corr_matrix.index)), corr_matrix.index)

# Show values inside cells
for i in range(len(corr_matrix.index)):
    for j in range(len(corr_matrix.columns)):
        plt.text(
            j, i,
            f"{corr_matrix.iloc[i, j]:.3f}",
            ha="center",
            va="center",
            color="black"
        )

plt.title("Pearson's Linear Correlation")
plt.tight_layout()
plt.savefig(r"../outputs/graphs/correlation_heatmap_exact.png")
plt.show()


# =========================================================
# Function for scatter plot + trend line
# =========================================================
def scatter_with_trend(x, y, x_label, y_label, title, file_name, r_value):
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, alpha=0.5)

    # Trend line
    m, b = np.polyfit(x, y, 1)
    x_sorted = np.sort(x)
    plt.plot(
        x_sorted,
        m * x_sorted + b,
        linestyle="--",
        linewidth=2,
        label=f"Trend line (r = {r_value:.3f})"
    )

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.tight_layout()
    plt.savefig(file_name)
    plt.show()


# =========================================================
# 2. Merchandise Spend vs Drink Spend
# =========================================================
scatter_with_trend(
    audience_df["Merchandise_Spend"],
    audience_df["Drink_Spend"],
    "Merchandise Spend (USD)",
    "Drink Spend (USD)",
    "Merchandise Spend vs Drink Spend",
    r"../outputs/graphs/merchandise_vs_drink_scatter.png",
    corr_matrix.loc["Merchandise_Spend", "Drink_Spend"]
)


# =========================================================
# 3. Ticket Price vs Satisfaction Score
# =========================================================
scatter_with_trend(
    audience_df["Ticket_Price"],
    audience_df["Satisfaction_Score"],
    "Ticket Price (USD)",
    "Satisfaction Score",
    "Ticket Price vs Satisfaction Score",
    r"../outputs/graphs/ticketprice_vs_satisfaction_scatter.png",
    corr_matrix.loc["Ticket_Price", "Satisfaction_Score"]
)


# =========================================================
# 4. Ticket Price vs Merchandise Spend
# =========================================================
scatter_with_trend(
    audience_df["Ticket_Price"],
    audience_df["Merchandise_Spend"],
    "Ticket Price (USD)",
    "Merchandise Spend (USD)",
    "Ticket Price vs Merchandise Spend",
    r"../outputs/graphs/ticketprice_vs_merchandise_scatter.png",
    corr_matrix.loc["Ticket_Price", "Merchandise_Spend"]
)


# =========================================================
# 5. Ticket Price vs Drink Spend
# =========================================================
scatter_with_trend(
    audience_df["Ticket_Price"],
    audience_df["Drink_Spend"],
    "Ticket Price (USD)",
    "Drink Spend (USD)",
    "Ticket Price vs Drink Spend",
    r"../outputs/graphs/ticketprice_vs_drink_scatter.png",
    corr_matrix.loc["Ticket_Price", "Drink_Spend"]
)

print("\nAll graphs and tables saved successfully.")