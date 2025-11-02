# 3. Sum of Series using Functions
# a. 1 + 2 + 3 + ... + n
# b. 1! + 2! + 3! + ... + n!# c. 1¹ + 2² + 3³ + ... + nⁿ

import math

def sum_n(n):
    return sum(range(1, n + 1))

def sum_factorial(n):
    total = 0
    for i in range(1, n + 1):
        total += math.factorial(i)
    return total

def sum_power(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total

n = int(input("Enter n: "))
print("Sum of 1+2+...+n =", sum_n(n))
print("Sum of 1!+2!+...+n! =", sum_factorial(n))
print("Sum of 1^1+2^2+...+n^n =", sum_power(n))

