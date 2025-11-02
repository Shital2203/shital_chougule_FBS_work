# 8.3 Series Calculations
import math

# c. Geometric series (1 + 2 + 4 + 8 + ... to n terms, ratio=2)
n = int(input("Enter number of terms for geometric series: "))
sum_geo = 0
term = 1
for i in range(n):
    sum_geo += term
    term *= 2
print("Sum of geometric series =", sum_geo)


