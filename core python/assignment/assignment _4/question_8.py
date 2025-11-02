# 8. Numbers divisible by 7 and multiple of 5 in rang

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print("Numbers divisible by 7 and multiple of 5 are:")
for i in range(start, end + 1):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end=" ")
print()

