import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
audience_df = pd.read_excel(r"../data/Company_X_Audience.xlsx")
show_df = pd.read_excel(r"../data/Company_X_ShowData.xlsx")

# Select only numerical columns
audience_num = audience_df.select_dtypes(include=["int64", "float64"])
show_num = show_df.select_dtypes(include=["int64", "float64"])

# Create summary statistics tables
audience_summary = audience_num.describe().T[["min", "25%", "50%", "75%", "max", "std"]]
show_summary = show_num.describe().T[["min", "25%", "50%", "75%", "max", "std"]]

# Rename columns for clarity
audience_summary.columns = ["Min", "Q1 (25%)", "Median (50%)", "Q3 (75%)", "Max", "Std Dev"]
show_summary.columns = ["Min", "Q1 (25%)", "Median (50%)", "Q3 (75%)", "Max", "Std Dev"]

# Round values
audience_summary = audience_summary.round(2)
show_summary = show_summary.round(2)

# Print results neatly
print("=" * 100)
print("SUMMARY STATISTICS TABLE - COMPANY_X_AUDIENCE")
print("=" * 100)
print(audience_summary.to_string())

print("\n" + "=" * 100)
print("SUMMARY STATISTICS TABLE - COMPANY_X_SHOWDATA")
print("=" * 100)
print(show_summary.to_string())

# Save to CSV
audience_summary.to_csv(r"../outputs/tables/audience_summary_statistics.csv")
show_summary.to_csv(r"../outputs/tables/showdata_summary_statistics.csv")

# Function to save dataframe as image
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
    audience_summary,
    "Summary Statistics Table - Company_X_Audience",
    r"../outputs/tables/audience_summary_statistics.png"
)

save_table_as_image(
    show_summary,
    "Summary Statistics Table - Company_X_ShowData",
    r"../outputs/tables/showdata_summary_statistics.png"
)

print("\nTables saved successfully in outputs/tables/")
print("- CSV files saved")
print("- PNG table images saved")