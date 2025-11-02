 # 8.2 Series Calculations

import math

# b. N + N^2 + N^3 + ... + N^N
N = int(input("Enter N for power series: "))
sum_power = 0
for i in range(1, N + 1):
    sum_power += N ** i
print("Sum of power series =", sum_power)
