import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
audience_df = pd.read_excel(r"../data/Company_X_Audience.xlsx")

# Filter repeat visitors only
repeat_visitors = audience_df[audience_df["Repeat_Visit"] == 1]

# Calculate average spending
avg_merch = repeat_visitors["Merchandise_Spend"].mean()
avg_drink = repeat_visitors["Drink_Spend"].mean()

# Create summary dataframe
spend_summary = pd.DataFrame({
    "Category": ["Merchandise_Spend", "Drink_Spend"],
    "Average_Spend": [avg_merch, avg_drink]
})

# Print results
print("=" * 70)
print("AVERAGE SPENDING OF REPEAT VISITORS (USD)")
print("=" * 70)
print(spend_summary)

# Function to show both percentage and actual amount in USD
def autopct_with_amount(values):
    def my_format(pct):
        total = sum(values)
        amount = pct * total / 100
        return f"{pct:.1f}%\n(USD {amount:.2f})"
    return my_format

# Plot pie chart
plt.figure(figsize=(8, 6))
plt.pie(
    spend_summary["Average_Spend"],
    labels=["Merchandise Spend", "Drink Spend"],
    autopct=autopct_with_amount(spend_summary["Average_Spend"]),
    startangle=90
)

plt.title("Average Merchandise vs Drink Spend Among Repeat Visitors (USD)")
plt.tight_layout()

# Save graph
plt.savefig(r"../outputs/graphs/repeat_visitors_spend_pie.png")
plt.show()