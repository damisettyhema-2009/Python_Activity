start_day = 2
days = 30

print("Mon Tue Wed Thu Fri Sat Sun")
print("    " * start_day, end="")

position = start_day

for day in range(1, days + 1):
    print(f"{day:3}", end=" ")

    position += 1

    if position == 7:
        print()
        position = 0

if position != 0:
    print()