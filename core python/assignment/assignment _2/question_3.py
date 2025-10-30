feet = float(input("Enter distance in feet: "))
inches = float(input("Enter remaining inches: "))

# 1 foot = 0.3048 meter, 1 inch = 2.54 cm
meters = feet * 0.3048 + inches * 0.0254
centimeters = meters * 100
print("Distance =", meters, "meters or", centimeters, "centimeters")
