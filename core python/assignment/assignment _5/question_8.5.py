# 8.3 Series Calculations
import math

# e. x - x²/3 + x³/5 - x⁴/7 + ... up to n terms
x = float(input("Enter value of x: "))
n = int(input("Enter number of terms: "))
sum_series = 0
sign = 1
den = 1

for i in range(1, n + 1):
    sum_series += sign * (x ** i) / den
    sign *= -1
    den += 2

print("Sum of alternating series (e) =", round(sum_series, 2))
