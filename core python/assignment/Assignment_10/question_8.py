#Write a program to create a duplicate of an existing list. It should not point to same list.
n = int(input("Enter how many elements you want in list: "))    
original_list = []
for i in range(n):
    num = int(input("Enter element: "))
    original_list.append(num)
duplicate_list = []
for item in original_list:
    duplicate_list.append(item)
print("Original List:", original_list)
print("Duplicate List:", duplicate_list)
