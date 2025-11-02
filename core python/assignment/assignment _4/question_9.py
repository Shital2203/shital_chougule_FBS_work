
# 9. Numbers in range divisible by given number

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
num = int(input("Enter number to check divisibility: "))

print("Numbers divisible by", num, "are:")
for i in range(start, end + 1):
    if i % num == 0:
        print(i, end=" ")
print()

