# Program to find area and circumference of a circle

import math  # for using the value of π (pi)

# Input radius
radius = float(input("Enter the radius of the circle: "))

# Calculate area and circumference
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

# Display results
print(f"Area of the circle = {area:.2f}")
print(f"Circumference of the circle = {circumference:.2f}")
