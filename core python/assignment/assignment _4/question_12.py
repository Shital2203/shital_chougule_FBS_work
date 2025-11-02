
# 12. Print Armstrong numbers within given range
# (Armstrong number = sum of cube of digits = number)

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("Armstrong numbers between", start, "and", end, "are:")
for num in range(start, end + 1):
    temp = num
    sum_pow = 0
    digits = len(str(num))
    while temp > 0:
        digit = temp % 10
        sum_pow += digit ** digits
        temp //= 10
    if num == sum_pow:
        print(num, end=" ")
print()