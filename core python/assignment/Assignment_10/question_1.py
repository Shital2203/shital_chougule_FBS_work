#Write a program to find sum of all elements of list
n = int(input("Enter the number of elements: "))
a = []     
for i in range(n):
    b = int(input("Enter element: "))
    a.append(b) 
c = sum(a)
print("Sum of the elements is:", c) 
