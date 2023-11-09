'''Phone number(D101)
In this exercise, you will learn how to perform basic input and output. 
Also, you will be able to try the HKOI Online Judge system.
Write a program to read a 8-digit Hong Kong phone number and determine whether 
it is a fixed line number (numbers that start with 2 or 3) or a mobile number 
(numbers that start with 5, 6 or 9).
'''
a = input()
aw = int(a[0])

if aw in [2, 3]:
    print("Fixed")
elif aw in [5, 6, 9]:
    print("Mobile")
else:
    raise Exception("unexpected value")
