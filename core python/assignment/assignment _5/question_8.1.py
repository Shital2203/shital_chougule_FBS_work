 # 8.1 Series Calculations

import math

# a. 1! + 2! + 3! + ... + n!
n = int(input("Enter n for factorial series: "))
sum_fact = 0
for i in range(1, n + 1):
    sum_fact += math.factorial(i)
print("Sum of factorial series =", sum_fact)

