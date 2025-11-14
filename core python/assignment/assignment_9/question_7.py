## Write a recursive function to calculate the sum of digits of a number.
def sum_digits(num):
    if num == 0:
        return 0
    else:
        return num % 10  + sum_digits(num // 10)

num = int(input("Enter a number: "))
print("Sum of digits:", sum_digits(num))
