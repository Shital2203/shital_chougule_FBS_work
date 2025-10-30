# 11. Calculate total ticket amount with discounts

total = 0
ticket_price = float(input("Enter per person ticket price: "))

for i in range(5):
    age = int(input(f"Enter age of person {i+1}: "))

    if age < 12:
        total += ticket_price * 0.7  # 30% discount
    elif age > 59:
        total += ticket_price * 0.5  # 50% discount
    else:
        total += ticket_price        # full price

print("Total ticket amount =", total)

