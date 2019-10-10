'''Bus fare (D102)
In Hong Kong, children under the age of 12 can ride the bus with half fare.
The amount is rounded up to the nearest ten cents.
For example, if the full fare is $9.3,
the half fare would be $4.7.
Write a program to display the half fare.
'''

import math
import re
a = input()
b = re.sub('\$','',a)
# print(b) # Debug only
ba = float(b)
c = ba / 2
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
d = round_up(c, 1)

# print(c) #debug
print('${}'.format(d))