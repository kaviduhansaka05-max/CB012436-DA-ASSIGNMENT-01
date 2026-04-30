import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
audience_df = pd.read_excel(r"../data/Company_X_Audience.xlsx")

# Count audience members by seating region
seating_counts = audience_df["Seating_Region"].value_counts()

# Print results
print("=" * 70)
print("ATTENDANCE ACROSS DIFFERENT SEATING REGIONS")
print("=" * 70)
print(seating_counts)

# Plot bar chart
plt.figure(figsize=(10, 6))
seating_counts.plot(kind="bar")
plt.title("Attendance Across Different Seating Regions")
plt.xlabel("Seating Region")
plt.ylabel("Number of Audience Members")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r"../outputs/graphs/seating_region_attendance.png")
plt.show()