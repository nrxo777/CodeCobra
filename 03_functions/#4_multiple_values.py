import math

def circle(r):
    _area = (math.pi * r ** 2)
    area = round(_area, 2)
    _circum = (2 * math.pi * r)
    circum = round(_circum, 2)
    
    return area, circum

a, c = circle(3)
print("Area: ", a, "Circumference: ", c)