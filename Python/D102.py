'''Bus fare (D102)
In Hong Kong, children under the age of 12 can ride the bus with half fare.
The amount is rounded up to the nearest ten cents.
For example, if the full fare is $9.3,
the half fare would be $4.7.
Write a program to display the half fare.
'''

# from math import *
import re
a = input()
b = re.sub('$','',a)
# print(b) # Debug only
ba = float(b)
c = ba / 2



# print(c) #debug
print('${}'.format(c))
