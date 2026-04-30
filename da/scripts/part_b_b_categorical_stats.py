import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
audience_df = pd.read_excel(r"../data/Company_X_Audience.xlsx")
show_df = pd.read_excel(r"../data/Company_X_ShowData.xlsx")

# Select categorical columns
audience_cat = audience_df.select_dtypes(include=["object", "string"])
show_cat = show_df.select_dtypes(include=["object", "string"])

# Create summary tables for categorical features
audience_cat_summary = audience_cat.describe().T[["count", "unique", "top", "freq"]]
show_cat_summary = show_cat.describe().T[["count", "unique", "top", "freq"]]

# Rename columns
audience_cat_summary.columns = ["Count", "Unique Categories", "Most Frequent Category", "Frequency"]
show_cat_summary.columns = ["Count", "Unique Categories", "Most Frequent Category", "Frequency"]

# Print neatly
print("=" * 100)
print("CATEGORICAL SUMMARY TABLE - COMPANY_X_AUDIENCE")
print("=" * 100)
print(audience_cat_summary.to_string())

print("\n" + "=" * 100)
print("CATEGORICAL SUMMARY TABLE - COMPANY_X_SHOWDATA")
print("=" * 100)
print(show_cat_summary.to_string())

# Save CSV files
audience_cat_summary.to_csv(r"../outputs/tables/audience_categorical_summary.csv")
show_cat_summary.to_csv(r"../outputs/tables/showdata_categorical_summary.csv")

# Function to save table as image
def save_table_as_image(df, title, filename):
    fig, ax = plt.subplots(figsize=(12, len(df) * 0.6 + 1.5))
    ax.axis("off")
    table = ax.table(
        cellText=df.values,
        rowLabels=df.index,
        colLabels=df.columns,
        cellLoc="center",
        loc="center"
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)
    plt.title(title, fontsize=12, pad=20)
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches="tight")
    plt.close()

# Save table images
save_table_as_image(
    audience_cat_summary,
    "Categorical Summary Table - Company_X_Audience",
    r"../outputs/tables/audience_categorical_summary.png"
)

save_table_as_image(
    show_cat_summary,
    "Categorical Summary Table - Company_X_ShowData",
    r"../outputs/tables/showdata_categorical_summary.png"
)

print("\nCategorical summary tables saved successfully in outputs/tables/")