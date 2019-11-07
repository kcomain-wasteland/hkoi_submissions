'''Story generator(D301)
In this section, you will learn about strings. 
A string a sequence of characters. Examples of strings are apple, 
Chan Tai Man and 123.456 (textual representation of numbers). 
As the first exercise, let's learn how to input and output strings.

Write a program to input several English words, and compose (output) a story using those words.
'''
a = input()
b = input()
c = input()
d = input()
e = input()
reply = 'My friends name is {}, he goes somewhere in {} and he eats {} daily. Today he went to school by {} to {}.'.format(a,b,c,d,e)
print(reply)