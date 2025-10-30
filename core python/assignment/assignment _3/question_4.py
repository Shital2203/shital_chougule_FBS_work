# 4. Check if triangle (by sides) is valid or not

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Triangle is valid")
else:
    print("Triangle is not valid")

