# 3. Ticket Calculation with Discounts

num = int(input("Enter number of passengers: "))
ticket_price = float(input("Enter per ticket cost: "))

total = 0
for i in range(num):
    age = int(input(f"Enter age of passenger {i+1}: "))
    if age < 12:
        total += ticket_price * 0.7   # 30% discount
    elif age > 59:
        total += ticket_price * 0.5   # 50% discount
    else:
        total += ticket_price         # full price

print("Total Ticket Amount = Rs.", round(total, 2))

