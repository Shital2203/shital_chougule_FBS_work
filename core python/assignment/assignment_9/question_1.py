# Function to find factorial using recursion
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

# Function to find sum of factorial series using recursion
def sum_series(n):
    if n == 0:
        return 0
    else:
        return fact(n) + sum_series(n - 1)

n = int(input("Enter the value of n: "))
print("Sum of series =", sum_series(n))
