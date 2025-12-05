#Write a program to reverse the list.
def reverse_list(input_list):
    return input_list[::-1] 

input_list = [1, 2, 3, 4, 5]
print("Input List:", input_list)
reversed_list = reverse_list(input_list)    
print("Reversed List:", reversed_list)