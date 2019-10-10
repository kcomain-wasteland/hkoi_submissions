'''Area of triangle(D103)
There are many ways to calculate the area of a triangle.
'''
from math import sin,degrees,radians
a = float(input())
b = float(input())
cdeg = float(input())
print(degrees(sin(radians(cdeg))))
d = 0.5 * a * b * degrees(sin(radians(cdeg)))

e = round(float(d),3)
print(e)
# 1/2 ab sin c