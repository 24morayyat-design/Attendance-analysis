import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('attendance.csv')

TOTAL_CLASSES = 40

df['Total_Attended'] = df[['Maths','Physics','Chemistry','English','Computer']].sum(axis=1)
df['Total_Classes'] = TOTAL_CLASSES * 5
df['Attendance_%'] = (df['Total_Attended'] / df['Total_Classes']) * 100

subject_avg = (df[['Maths','Physics','Chemistry','English','Computer']].mean() / TOTAL_CLASSES) * 100

df['Status'] = np.where(df['Attendance_%'] >= 75, 'Regular', 'Irregular')

print("===== Student Attendance Summary =====\n")
print(df[['Name','Roll_No','Attendance_%','Status']])

print("\n===== Subject-wise Average Attendance (%) =====\n")
print(subject_avg)

plt.figure(figsize=(10,6))
plt.bar(df['Name'], df['Attendance_%'], color='skyblue')
plt.title('Overall Attendance Percentage per Student')
plt.xlabel('Student Name')
plt.ylabel('Attendance (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
subject_avg.plot(kind='bar', color='lightgreen')
plt.title('Average Attendance per Subject')
plt.xlabel('Subjects')
plt.ylabel('Attendance (%)')
plt.tight_layout()
plt.show()

status_counts = df['Status'].value_counts()
plt.figure(figsize=(5,5))
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90, colors=['#7FE9DE','#F5B7B1'])
plt.title('Regular vs Irregular Students')
plt.tight_layout()
plt.show()

df.to_csv('attendance_report.csv', index=False)
print("\n✅ Attendance report saved as 'attendance_report.csv'")
