# Write a program to remove duplicates from the list.
li=[34,5,4,76,34,56,3,4,5]
def remove_duplicates(input_list):
    return list(set(input_list))

print("Original List:", li)
print("List after removing duplicates:", remove_duplicates(li))