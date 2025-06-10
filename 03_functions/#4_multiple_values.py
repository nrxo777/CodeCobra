import math

def circle(r):
    _area = math.pi * r ** 2
    _circum = 2 * math.pi * r
    
    return _area, _circum

print(circle(4))