# 8.4 Series Calculations
import math

# d. S = a + a²/2 + a³/3 + ... + a¹⁰/10
a = float(input("Enter value of a: "))
sum_series = 0
for i in range(1, 11):
    sum_series += (a ** i) / i
print("Sum of series (d) =", round(sum_series, 2))

