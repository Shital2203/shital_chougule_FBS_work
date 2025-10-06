# Program to find the volume of a sphere

import math  # for using π (pi)

# Input radius
radius = float(input("Enter the radius of the sphere: "))

# Formula: Volume = (4/3) * π * r³
volume = (4/3) * math.pi * radius ** 3

# Display result
print(f"The volume of the sphere is: {volume:.2f}")
