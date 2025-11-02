#  Reverse of a number using Function

def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

n = int(input("Enter number: "))
print("Reversed number =", reverse_number(n))
