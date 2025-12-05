 # Program to print list after removing even numbers

n = int(input("Enter how many elements you want in list: "))
lst = []      
new_list = [] 

for i in range(n):
    num = int(input("Enter element: "))
    lst.append(num)

for x in lst:
    if x % 2 != 0:       
        new_list.append(x)


print("Original List:", lst)
print("List after removing even numbers:", new_list)
