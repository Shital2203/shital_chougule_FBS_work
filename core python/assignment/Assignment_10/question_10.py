#Write a program to remove all occurrences of a given element in the list without using inbuilt functions.
li=[3,4,5,6,3,7,9,7,6,7,4]
n =int(input("enter element to remove all accurances: "))

new_li = []
for i in li:
    if i != n:
        new_li.append(i)

print("list after removing all occurances of",n, "is:", new_li)
