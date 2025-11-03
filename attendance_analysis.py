import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('attendance.csv')
print("---- Attendance Data ----")
print(df)

df['Attendance_%'] = (df['Attended_Classes'] / df['Total_Classes']) * 100
print("\n---- Attendance with Percentage ----")
print(df)

avg_attendance = df['Attendance_%'].mean()
highest = df.loc[df['Attendance_%'].idxmax()]
lowest = df.loc[df['Attendance_%'].idxmin()]

print(f"\nAverage Class Attendance: {avg_attendance:.2f}%")
print(f"Highest Attendance: {highest['Name']} ({highest['Attendance_%']:.2f}%)")
print(f"Lowest Attendance: {lowest['Name']} ({lowest['Attendance_%']:.2f}%)")

defaulters = df[df['Attendance_%'] < 75]
print("\n---- Defaulters (Below 75%) ----")
print(defaulters)

plt.figure(figsize=(10,6))
plt.bar(df['Name'], df['Attendance_%'], color='skyblue')
plt.axhline(y=75, color='r', linestyle='--', label='Minimum Required (75%)')
plt.title('Student Attendance Percentage')
plt.xlabel('Students')
plt.ylabel('Attendance (%)')
plt.legend()
plt.tight_layout()
plt.show()

total_classes = df['Total_Classes'].sum()
attended_classes = df['Attended_Classes'].sum()
absent_classes = total_classes - attended_classes

plt.figure(figsize=(5,5))
plt.pie([attended_classes, absent_classes],
        labels=['Attended', 'Missed'],
        autopct='%1.1f%%', colors=['green','red'])
plt.title('Overall Class Attendance Distribution')
plt.tight_layout()
plt.show()

df.to_csv('attendance_analysis_output.csv', index=False)
print("\nAnalysis saved to 'attendance_analysis_output.csv'")