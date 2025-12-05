# Program to print numbers divisible by m and n from a list

# take size of list
size = int(input("Enter how many elements you want in list: "))

# create empty list
lst = []

# take list elements
for i in range(size):
    num = int(input("Enter element: "))
    lst.append(num)

# take m and n values
m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))

print("Numbers divisible by", m, "and", n, "are:")

# check divisibility
for x in lst:
    if x % m == 0 and x % n == 0:
        print(x)
    else:
        print(f"{x} is not divisible by {m} and {n}")   
        
