
## Write a recursive function to calculate the factorial of a number.
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

num = int(input("Enter number: "))
print("Factorial of", num, "is", fact(num))
