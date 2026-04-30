import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ----------------------------
# FILE PATHS
# ----------------------------
files = {
    "ShowData": "../data/Company_X_ShowData.xlsx",
    "AudienceData": "../data/Company_X_Audience.xlsx"
}

# ----------------------------
# LOAD DATA
# ----------------------------
def load_data(file_path):
    excel = pd.ExcelFile(file_path)
    sheet = excel.sheet_names[0]
    return pd.read_excel(file_path, sheet_name=sheet)

# ----------------------------
# DATASET SIZE GRAPH
# ----------------------------
def dataset_size_plot(summary):
    names = list(summary.keys())
    rows = [summary[n]["rows"] for n in names]

    plt.figure()
    plt.bar(names, rows)
    plt.title("Dataset Size Comparison")
    plt.ylabel("Number of Rows")

    for i, v in enumerate(rows):
        plt.text(i, v + 5, str(v), ha='center')

    plt.savefig("../outputs/graphs/dataset_size.png")
    plt.show()

# ----------------------------
# MISSING VALUES GRAPH
# ----------------------------
def missing_plot(df, name):
    missing = df.isnull().sum()

    plt.figure(figsize=(8,4))
    plt.bar(missing.index, missing.values)
    plt.title(f"Missing Values - {name}")
    plt.xticks(rotation=45)

    plt.savefig(f"../outputs/graphs/{name}_missing.png")
    plt.show()

# ----------------------------
# DATA TYPE GRAPH
# ----------------------------
def dtype_plot(df, name):
    counts = df.dtypes.value_counts()

    plt.figure()
    counts.plot(kind='bar')
    plt.title(f"Data Type Distribution - {name}")

    plt.savefig(f"../outputs/graphs/{name}_dtype.png")
    plt.show()

# ----------------------------
# MAIN
# ----------------------------
summary = {}

for name, path in files.items():
    df = load_data(Path(path))

    summary[name] = {
        "rows": df.shape[0],
        "cols": df.shape[1]
    }

    missing_plot(df, name)
    dtype_plot(df, name)

dataset_size_plot(summary)

print("Graphs generated ✅")