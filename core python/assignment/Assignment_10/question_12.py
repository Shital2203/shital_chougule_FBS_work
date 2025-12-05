# Program to create three lists: numbers, their squares, and cubes

n = int(input("Enter how many elements: "))

numbers = []     
squares = []     
cubes = []       
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

    squares.append(num * num)         
    cubes.append(num * num * num)     

print("Numbers: ", numbers)
print("Squares: ", squares)
print("Cubes: ", cubes)
