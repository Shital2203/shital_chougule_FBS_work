#Write a program to create a new list from existing list which contains cube of each number of list without using inbuilt functions.

n = int(input("Enter how many elements you want in list: "))

original_list = []
cube_list = []
for i in range(n):
    num = int(input("Enter element: "))
    original_list.append(num)

for i in original_list:
    cube = i * i * i     # cube logic
    cube_list.append(cube)


print("Original List:", original_list)
print("Cube List:", cube_list)
