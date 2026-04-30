import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
show_df = pd.read_excel(r"../data/Company_X_ShowData.xlsx")

# Convert date column
show_df["Show_Date"] = pd.to_datetime(show_df["Show_Date"])

# Extract day and month names
show_df["Day_Name"] = show_df["Show_Date"].dt.day_name()
show_df["Month_Name"] = show_df["Show_Date"].dt.month_name()

# Correct order
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
month_order = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

# Average attendance by day
day_sales = show_df.groupby("Day_Name")["Attendance"].mean().reindex(day_order)

# Average attendance by month
month_sales = show_df.groupby("Month_Name")["Attendance"].mean().reindex(month_order)

# Print tables
print("=" * 90)
print("AVERAGE TICKET SALES BY DAY OF THE WEEK")
print("=" * 90)
print(day_sales.round(2))

print("\n" + "=" * 90)
print("AVERAGE TICKET SALES BY MONTH OF THE YEAR")
print("=" * 90)
print(month_sales.round(2))

# Bar chart by day
plt.figure(figsize=(10, 6))
plt.bar(day_sales.index, day_sales.values, edgecolor="black")
plt.title("Average Ticket Sales by Day of the Week")
plt.xlabel("Day of the Week")
plt.ylabel("Average Attendance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r"../outputs/graphs/ticket_sales_by_day.png")
plt.show()

# Bar chart by month
plt.figure(figsize=(12, 6))
plt.bar(month_sales.index, month_sales.values, edgecolor="black")
plt.title("Average Ticket Sales by Month of the Year")
plt.xlabel("Month")
plt.ylabel("Average Attendance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r"../outputs/graphs/ticket_sales_by_month.png")
plt.show()