transactions = [
    ("T101", 12000),
    ("T102", 75000),
    ("T101", 12000),
    ("T103", 25000),
    ("T104", 90000)
]

seen = []
suspicious = []

for tid, amount in transactions:
    reasons = []

    if tid in seen:
        reasons.append("Duplicate ID")

    if amount > 50000:
        reasons.append("Amount above ₹50000")

    if reasons:
        suspicious.append((tid, amount, reasons))

    seen.append(tid)

print("Suspicious transactions:")

for item in suspicious:
    print(item)