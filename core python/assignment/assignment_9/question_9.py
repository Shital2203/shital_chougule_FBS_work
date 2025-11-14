## Write a recursive function to calculate the power of a number.
def power(m, n):
    if n == 0:
        return 1
    else:
        return m * power(m, n - 1)

m = int(input("Enter base (m): "))
n = int(input("Enter power (n): "))
print(m, "raised to", n, "is", power(m, n))
