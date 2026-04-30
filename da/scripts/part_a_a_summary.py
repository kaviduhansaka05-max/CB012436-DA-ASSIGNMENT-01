import pandas as pd

# Load datasets
audience_df = pd.read_excel(r"../data/Company_X_Audience.xlsx")
show_df = pd.read_excel(r"../data/Company_X_ShowData.xlsx")

# COMPANY_X_AUDIENCE
print("=" * 70)
print("COMPANY_X_AUDIENCE DATASET SUMMARY")
print("=" * 70)

print("\n1. Dataset Shape")
print("Shape of Company_X_Audience dataset:", audience_df.shape)
print("Number of rows:", audience_df.shape[0])
print("Number of columns:", audience_df.shape[1])

print("\n2. Data Types and Structure")
audience_df.info()

print("\n3. Missing Values")
print(audience_df.isnull().sum())

print("\nColumns with missing values only:")
audience_missing = audience_df.isnull().sum()
print(audience_missing[audience_missing > 0])

# COMPANY_X_SHOWDATA

print("\n" + "=" * 70)
print("COMPANY_X_SHOWDATA DATASET SUMMARY")
print("=" * 70)

print("\n1. Dataset Shape")
print("Shape of Company_X_ShowData dataset:", show_df.shape)
print("Number of rows:", show_df.shape[0])
print("Number of columns:", show_df.shape[1])

print("\n2. Data Types and Structure")
show_df.info()

print("\n3. Missing Values")
print(show_df.isnull().sum())

print("\nColumns with missing values only:")
show_missing = show_df.isnull().sum()
print(show_missing[show_missing > 0])