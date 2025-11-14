
## Write a recursive function to calculate the sum of first n  numbers.
def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n - 1)

n = int(input("Enter n: "))
print("Sum of first", n, "numbers =", sum_n(n))
