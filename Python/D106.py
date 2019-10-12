'''Ordinal number(D106)
Write a program to the ordinal form of a number.
'''
from argparse import ArgumentParser
par = ArgumentParser()
par.add_argument("-n")
a = par.parse_args()
qqq = a.n

# a = str(input())
b = [k for k in qqq]
alen = len(qqq)
c = b[alen-1]
res = ''
# print(b)
# print('\n{}'.format(b[alen-1]))
# print(c)
if qqq == '11':
    res = qqq+'th'
elif qqq == '12':
    res = qqq+'th'
elif qqq == '13':
    res = qqq+'th'
else:
    if c == '1':
        res = qqq+'st'
    elif c == '2':
        res = qqq+'nd'
    elif c == '3':
        res = qqq+'rd'
    else:
        res = qqq+'th'
# print(res)
f = open("lastdep.txt", "a")
f.write(res+'\n')
f.close()