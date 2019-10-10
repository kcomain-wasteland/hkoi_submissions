'''Area of triangle(D103)
There are many ways to calculate the area of a triangle.
'''
from math import sin
a = int(input())
b = int(input())
cdeg = int(input())
d = (str((1/2)*a*b)+'{}'.format(sin(cdeg)))
e = round(d,3)
print(e)
# 1/2 ab sin c