import numpy as np
import pandas as pd

# Just some made-up students and subjects
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
subjects = ['Math', 'Science', 'History', 'English']

# Random grades between 40 and 100 (simulate real grades)
np.random.seed(0)
grades = np.random.randint(40, 101, size=(len(students), len(subjects)))

# Create DataFrame
df = pd.DataFrame(grades, columns=subjects, index=students)

print("🎓 Student Grades:\n")
print(df)
print("\n📊 Analysis:\n")

# Average grade per student
df['Average'] = df.mean(axis=1)
print("👉 Average grade per student:")
print(df['Average'])

# Average grade per subject
print("\n👉 Average grade per subject:")
print(df[subjects].mean())

# Highest scoring student
top_student = df['Average'].idxmax()
print(f"\n🏅 Top performer: {top_student} with average {df.loc[top_student, 'Average']:.2f}")

# Who failed any subject (less than 50)
print("\n🚨 Students who failed in at least one subject:")
fails = df[df[subjects].lt(50).any(axis=1)]
if not fails.empty:
    print(fails[subjects])
else:
    print("🎉 No failures! Everyone passed.")

# Save to CSV if needed
df.to_csv("student_grades.csv")
print("\n📁 Grades have been saved to 'student_grades.csv'")
