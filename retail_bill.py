items = [
    ("Laptop", "electronics", 40000, 1),
    ("Book", "book", 500, 3),
    ("Headphones", "electronics", 2000, 1)
]

subtotal = 0
tax = 0

for name, category, price, qty in items:
    amount = price * qty
    subtotal += amount

    if category == "electronics":
        rate = 0.18
    else:
        rate = 0.05

    tax += amount * rate
    print(name, "Amount: ₹", amount)

if subtotal > 5000:
    discount = min(subtotal * 0.10, 1000)
else:
    discount = 0

final_bill = subtotal - discount + tax

print("Subtotal: ₹", subtotal)
print("Discount: ₹", discount)
print("Tax: ₹", round(tax, 2))
print("Final Bill: ₹", round(final_bill, 2))