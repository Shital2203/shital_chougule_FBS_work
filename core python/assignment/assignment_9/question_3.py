## Write a recursive function to reverse a number.
def reverse_num(num, rev=0):
    if num == 0:
        return rev
    return reverse_num(num // 10, rev * 10 + num % 10)

num = int(input("Enter a number: "))
print("Reversed number:", reverse_num(num))
