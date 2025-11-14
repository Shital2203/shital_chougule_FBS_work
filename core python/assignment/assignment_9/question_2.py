## Write a recursive function to check whether a number is an Armstrong number or not.
def power(num, p):
    if p == 0:
        return 1
    return num * power(num, p - 1)

def armstrong(num, temp=None, digits=None):
    if temp is None:
        temp = num
        digits = len(str(num))
    if temp == 0:
        return 0
    return power(temp % 10, digits) + armstrong(num, temp // 10, digits)

num = int(input("Enter a number: "))
if num == armstrong(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
