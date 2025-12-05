#Accept a number from user and check if this element is present in the list ornot. Also tell how many times it is present in the list.

li = [2,4,5,6,7,8,4,5,2,2] 
ele=int(input("enter  element for check in list : "))
if ele in li:
    print('element is present in the list', ele,)
    print('number of same elements : ',li.count(ele))
    
else:
    print("not present")

