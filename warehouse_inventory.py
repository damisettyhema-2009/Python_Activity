products = ["Books", "Pens", "Bags"]

opening = [100, 200, 50]
incoming = [50, 100, 20]
dispatched = [80, 250, 40]
actual_closing = [70, 40, 30]

for i in range(len(products)):

    expected_closing = opening[i] + incoming[i] - dispatched[i]

    print("\nProduct:", products[i])
    print("Opening Stock:", opening[i])
    print("Incoming:", incoming[i])
    print("Dispatched:", dispatched[i])
    print("Expected Closing:", expected_closing)
    print("Actual Closing:", actual_closing[i])

    if expected_closing == actual_closing[i]:
        print("Status: No discrepancy")
    elif actual_closing[i] < expected_closing:
        shortage = expected_closing - actual_closing[i]
        print("Status: Shortage")
        print("Shortage Quantity:", shortage)
    else:
        surplus = actual_closing[i] - expected_closing
        print("Status: Surplus")
        print("Surplus Quantity:", surplus)
