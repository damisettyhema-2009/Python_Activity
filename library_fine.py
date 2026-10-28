records = [
    ("B101", 10),
    ("B102", 17),
    ("B103", 14),
    ("B104", 20)
]

allowed_days = 14
fine_per_day = 5
total_fine = 0

for book_id, days in records:

    overdue = max(0, days - allowed_days)
    fine = overdue * fine_per_day

    total_fine += fine

    print(
        book_id,
        "Days:", days,
        "Overdue:", overdue,
        "Fine: ₹", fine
    )

print("Total Fine: ₹", total_fine)