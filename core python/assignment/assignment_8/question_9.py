# Check Palindrome Number using Function
def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

# Function to check palindrome
def is_palindrome(num):
    return num == reverse_number(num)

# Main program
n = int(input("Enter number: "))
if is_palindrome(n):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

