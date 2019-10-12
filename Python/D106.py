'''Ordinal number(D106)
Write a program to the ordinal form of a number.
'''
a = str(input())
b = [k for k in a]
alen = len(a)
res = ''
# print(b)
# print('\n{}'.format(b[alen-1]))
if a == '11' or '12' or '13':
    res = a + 'th'
elif b[alen-1] == '1':
    res = a + 'st'
elif b[alen-1] == '2':
    res = a + 'nd'
elif b[alen-1] == '3':
    res = a + 'rd'
else:
    res = a + 'th'
print(res)