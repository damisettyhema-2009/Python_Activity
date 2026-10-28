courses = [
    ("Python", "Mon", 9, 10),
    ("Maths", "Mon", 10, 11),
    ("AI", "Tue", 9, 11),
    ("English", "Tue", 10, 12)
]

conflicts = []

for i in range(len(courses)):
    c1, d1, s1, e1 = courses[i]

    for j in range(i + 1, len(courses)):
        c2, d2, s2, e2 = courses[j]

        if d1 == d2 and s1 < e2 and s2 < e1:
            conflicts.append((c1, c2, d1))

if conflicts:
    print("Timetable conflicts:")

    for conflict in conflicts:
        print(conflict[0], "and", conflict[1], "on", conflict[2])
else:
    print("No timetable conflicts")