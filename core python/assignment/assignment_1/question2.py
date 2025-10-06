# Program 2: Calculates the area of a rectangle.

# Get the dimensions from the user
try:
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    
    # Calculate the area: Area = Length * Breadth
    area = length * breadth
    
    # Print the result
    print(f"\nLength: {length:.2f}")
    print(f"Breadth: {breadth:.2f}")
    print(f"The calculated Area of the rectangle is: {area:.2f} square units.")

except ValueError:
    print("Error: Invalid input. Please ensure you enter valid numbers.")
