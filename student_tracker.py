
import pandas as pd
import matplotlib.pyplot as plt

# Student data
data = {
    "Student": ["Ravi", "Sita", "Raju", "Priya", "Kiran"],
    "Maths": [85, 70, 45, 95, 60],
    "Science": [90, 75, 50, 90, 65],
    "English": [80, 80, 55, 85, 70]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate total and average
subjects = ["Maths", "Science", "English"]
df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1)

# Display student performance
print("\nSTUDENT PERFORMANCE REPORT")
print(df.to_string(index=False))

# Display class average
print("\nClass Average:", round(df["Average"].mean(), 2))

# Create a bar chart
plt.bar(df["Student"], df["Average"])
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Performance Tracker")
plt.ylim(0, 100)
plt.tight_layout()
plt.show()