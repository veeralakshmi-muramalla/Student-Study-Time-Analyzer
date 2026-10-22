import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("study_data.csv")

print("===== STUDENT STUDY TIME ANALYZER =====")

print("\nStudy Data:")
print(data)

total_hours = data["Study_Hours"].sum()
average_hours = data["Study_Hours"].mean()

highest_subject = data.loc[data["Study_Hours"].idxmax(), "Subject"]
highest_hours = data["Study_Hours"].max()

lowest_subject = data.loc[data["Study_Hours"].idxmin(), "Subject"]
lowest_hours = data["Study_Hours"].min()

print("\n===== ANALYSIS =====")

print("Total Study Hours:", total_hours)
print("Average Study Hours:", round(average_hours, 2))

print("Most Studied Subject:",
      highest_subject, "-", highest_hours, "hours")

print("Least Studied Subject:",
      lowest_subject, "-", lowest_hours, "hours")

print("\n===== SUGGESTION =====")

if average_hours < 7:
    print("You should try to increase your study time.")
else:
    print("Good! You are maintaining a good study routine.")

plt.bar(data["Subject"], data["Study_Hours"])

plt.title("Student Study Time")
plt.xlabel("Subjects")
plt.ylabel("Study Hours")

plt.xticks(rotation=30)
plt.tight_layout()

plt.show()