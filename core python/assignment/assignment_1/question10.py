# Program to find the area of an equilateral triangle

import math  # for using square root function

# Input side length
side = float(input("Enter the side of the equilateral triangle: "))

# Formula: Area = (√3 / 4) * side²
area = (math.sqrt(3) / 4) * side ** 2

# Display result
print(f"The area of the equilateral triangle is: {area:.2f}")
