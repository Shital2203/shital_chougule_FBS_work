# 4. Check if number is Armstrong Number


n = int(input("Enter a number: "))
temp = n
sum_pow = 0
digits = len(str(n))

while temp > 0:
    digit = temp % 10
    sum_pow += digit ** digits
    temp //= 10

if n == sum_pow:
    print("Armstrong Number ✅")
else:
    print("Not an Armstrong Number ❌")

