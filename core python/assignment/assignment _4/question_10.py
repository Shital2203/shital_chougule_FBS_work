
# 10. Check if number is Perfect Number
# (Perfect number = sum of divisors = number)

n = int(input("Enter a number: "))
sum_div = 0
for i in range(1, n):
    if n % i == 0:
        sum_div += i
if sum_div == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
