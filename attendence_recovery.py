attended = 60
total = 90
required = 75

current = attended / total * 100
needed = 0

while current < required:
    attended += 1
    total += 1
    needed += 1
    current = attended / total * 100

print("Current attendance:", round(60 / 90 * 100, 2), "%")
print("Classes required:", needed)
print("Attendance after recovery:", round(current, 2), "%")