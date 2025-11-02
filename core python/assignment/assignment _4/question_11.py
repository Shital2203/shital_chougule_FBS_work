# 11. Check if number is Strong Number
# (Strong number = sum of factorials of digits = number)
# Example: 145 = 1! + 4! + 5! = 14

n = int(input("Enter a number: "))
temp = n
sum_fact = 0

while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    sum_fact += fact
    temp //= 10

if sum_fact == n:
    print("Strong Number")
else:
    print("Not a Strong Number")
