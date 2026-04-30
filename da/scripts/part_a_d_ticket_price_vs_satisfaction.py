import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
audience_df = pd.read_excel(r"../data/Company_X_Audience.xlsx")

# Scatter graph
plt.figure(figsize=(10, 6))
plt.scatter(audience_df["Ticket_Price"], audience_df["Satisfaction_Score"], alpha=0.6)

plt.title("Relationship Between Ticket Price and Satisfaction Score")
plt.xlabel("Ticket Price (USD)")
plt.ylabel("Satisfaction Score")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()

# Save graph
plt.savefig(r"../outputs/graphs/ticket_price_vs_satisfaction_scatter.png")
plt.show()