#  Area of Circle using Function

import math

def area_circle(radius):
    return math.pi * radius ** 2

r = float(input("Enter radius: "))
print("Area of circle =", round(area_circle(r), 2))



