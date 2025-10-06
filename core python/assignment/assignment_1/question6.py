# Program to find the third angle of a triangle

# Input two angles from user
angle1 = float(input("Enter first angle of the triangle: "))
angle2 = float(input("Enter second angle of the triangle: "))

# Calculate third angle
angle3 = 180 - (angle1 + angle2)

# Display result
print(f"The third angle of the triangle is: {angle3}°")
