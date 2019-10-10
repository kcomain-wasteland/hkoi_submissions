'''Simple calculator(D108)
Write a program to evaluate a simple arithmetic expression.
The specifications of the expression are as follows:

The expression consists of 3 operands and 2 operators.
The operands are integers between 0 and 100 inclusive.
The operators are either +(plus), -(minus) or *(times).
The expression does not contain any brackets.
'''
# So DIFFICULT AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
import re
a = input()
bst = [c for c in a]
first = ''
sec = ''
for i in bst:
    if first == '':
        if i == '+':
            first = '+'
        elif i == '-':
            first = '-'
        elif i == '*':
            first = '*'
        elif i == '/':
            first = '/'
    else:
        if i == '+':
            sec = '+'
        elif i == '-':
            sec = '-'
        elif i == '*':
            sec = '*'
        elif i == '/':
            sec = '/'
# print('First: {}'.format(first))
# print('Second: {}'.format(sec))
regex = r'[\+\-\*\/]'
b = re.sub(regex,'',a)
c = b.split(' ')    
result = 0
# print(c)
if first == '+':
    if sec == '+':
        result = int(c[0]) + int(c[2]) + int(c[4])
    elif sec == '-':
        result = int(c[0]) + int(c[2]) - int(c[4])
    elif sec == '*':
        result = int(c[0]) + int(c[2]) * int(c[4])
    elif sec == '/':
        result = int(c[0]) + int(c[2]) / int(c[4])
elif first == '-':
    if sec == '+':
        result = int(c[0]) - int(c[2]) + int(c[4])
    elif sec == '-':
        result = int(c[0]) - int(c[2]) - int(c[4])
    elif sec == '*':
        result = int(c[0]) - int(c[2]) * int(c[4])
    elif sec == '/':
        result = int(c[0]) - int(c[2]) / int(c[4])
elif first == '*':
    if sec == '+':
        result = int(c[0]) * int(c[2]) + int(c[4])
    elif sec == '-':
        result = int(c[0]) * int(c[2]) - int(c[4])
    elif sec == '*':
        result = int(c[0]) * int(c[2]) * int(c[4])
    elif sec == '/':
        result = int(c[0]) * int(c[2]) / int(c[4])
elif first == '/':
    if sec == '+':
        result = int(c[0]) / int(c[2]) + int(c[4])
    elif sec == '-':
        result = int(c[0]) / int(c[2]) - int(c[4])
    elif sec == '*':
        result = int(c[0]) / int(c[2]) * int(c[4])
    elif sec == '/':
        result = int(c[0]) / int(c[2]) / int(c[4])
print(result)