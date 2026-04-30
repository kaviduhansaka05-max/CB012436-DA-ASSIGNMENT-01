import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
audience_df = pd.read_excel(r"../data/Company_X_Audience.xlsx")

# Count audience members by country
top_5_countries = audience_df["Country"].value_counts().head(5)

# Print results
print("=" * 60)
print("TOP 5 COUNTRIES CONTRIBUTING THE MOST AUDIENCE MEMBERS")
print("=" * 60)
print(top_5_countries)

# Create column bar chart
plt.figure(figsize=(10, 6))
top_5_countries.plot(kind="bar")
plt.title("Top 5 Countries Contributing the Most Audience Members")
plt.xlabel("Country")
plt.ylabel("Number of Audience Members")
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart
plt.savefig(r"../outputs/graphs/top_5_countries_bar_chart.png")
plt.show()