## Write a recursive function to check whether a number is prime or not.
def is_prime(num, i=2):
    if num <= 2:
        return True if num == 2 else False
    elif num % i == 0:
        return False
    elif i * i > num:
        return True
    return is_prime(num, i + 1)

num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a Prime number.")
else:
    print(num, "is not a Prime number.")
