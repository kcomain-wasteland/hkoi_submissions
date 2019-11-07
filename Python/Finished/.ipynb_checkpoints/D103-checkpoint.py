'''Area of triangle(D103)
There are many ways to calculate the area of a triangle.
'''
from math import sin,degrees,radians
a = int(input())
b = int(input())
cdeg = int(input())
# print(sin(radians(cdeg)))
d = 0.5 * a * b * sin(radians(cdeg))
# print('Cdeg sin: {}'.format(degrees(sin(cdeg))))
# print('d = {}'.format(d))
e = round(float(d),3)
f = len(str(e))
g = str(e)
if f == 3:
    g += '00'
if f == 2:
    g += '0'
print(g)
# 1/2 ab sin c