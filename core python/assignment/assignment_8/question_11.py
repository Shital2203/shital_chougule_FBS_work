#  Check Armstrong Number using Function

def is_armstrong(num):
    digits = len(str(num))
    total = 0
    temp = num
    while temp > 0:
        total += (temp % 10) ** digits
        temp //= 10
    return total == num

n = int(input("Enter number: "))
if is_armstrong(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")