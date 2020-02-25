'''String length and words(D302)
Write a program to read a string and output:
> The length of the string
> Number of words in the string. There is exactly one space between words.
'''

inp = input()

words = len(inp.split(' '))
chars = len([c for c in inp])

print('{}\n{}'.format(chars,words))