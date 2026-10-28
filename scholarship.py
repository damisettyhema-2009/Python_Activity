applicants = [
    ("Anu", [82, 76, 80], 82, 250000),
    ("Ravi", [75, 62, 70], 78, 280000),
    ("Kiran", [90, 88, 92], 85, 220000),
    ("Meena", [85, 55, 88], 90, 200000)
]

eligible = []

for name, marks, attendance, income in applicants:
    aggregate = sum(marks) / len(marks)

    if aggregate >= 75 and min(marks) >= 60 and attendance >= 75 and income <= 300000:
        eligible.append((name, aggregate, attendance, income))

eligible.sort(key=lambda x: x[1], reverse=True)

print("Eligible Scholarship Applicants:")

for rank, student in enumerate(eligible, 1):
    print(rank, student[0], "Aggregate:", round(student[1], 2))