# Write a program to find the second largest element in the list without removing.
a = [5,98,45,63,54,78,43,9,23]
max_element = max(a)
second_largest = max(x for x in a if x != max_element)
print("The second largest element in the list is:", second_largest)
print(a)   
