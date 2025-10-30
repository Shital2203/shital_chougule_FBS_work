# 12. Check if 3-digit number is palindrome or not

num = int(input("Enter a three-digit number: "))

rev = int(str(num)[::-1])

if num == rev:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")
