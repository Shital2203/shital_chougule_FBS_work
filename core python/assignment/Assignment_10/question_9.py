#Write a program of having n number of elements in the list and find out evenand odd elements in that list and then create two separate lists which will have even elements and other will have odd elements.
n= int(input("enter element in list: "))
original_list=[]
for i in range(n):
    num = int(input("enter element "))
    original_list.append(num)
even_list=[]
odd_list=[]
for i in original_list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("original list:",original_list)
print("even list",even_list)
print("odd list",odd_list)

