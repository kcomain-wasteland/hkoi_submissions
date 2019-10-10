'''Area of triangle(D103)
There are many ways to calculate the area of a triangle.
'''
from math import sin,degrees
a = int(input())
b = int(input())
cdeg = int(input())
print(degrees(sin(cdeg)))
d = 0.5 * a * b * degrees(sin(cdeg))
# print('Cdeg sin: {}'.format(degrees(sin(cdeg))))
# print('d = {}'.format(d))
e = round(float(d),3)
print(e)
# 1/2 ab sin c