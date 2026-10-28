subjects = ["Python", "Maths", "AI", "English"]

exam1 = [55, 62, 48, 70]
exam2 = [68, 60, 52, 78]

improvements = []

for i in range(len(subjects)):
    improvements.append(exam2[i] - exam1[i])
    print(subjects[i], "Improvement:", improvements[i])

average = sum(exam2) / len(exam2)

weak = []

for i in range(len(subjects)):
    if (exam1[i] + exam2[i]) / 2 < 50:
        weak.append(subjects[i])

if average >= 80:
    category = "Excellent"
elif average >= 60:
    category = "Good"
else:
    category = "Needs Improvement"

print("Final average:", round(average, 2))
print("Weak subjects:", weak)
print("Performance:", category)