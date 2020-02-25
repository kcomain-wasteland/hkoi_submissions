#!/usr/bin/python3.5
# Check Digit(D305)
0

# '''Check digit calculation(D305)
# The Hong Kong Identity Card consists of 1 or 2 English letter(s) and 6 numeric digits.
# A check digit, which could be 0 to 9 or A, is appended in brackets. It is calculated as follows:
#
# For letters, A is converted to value 10, B to value 11, and so on. (Similar to base 36).
# If there are two letters, i.e. L1L2D1D2D3D4D5D6.
# The sum is s=9L1+8L2+7D1+6D2+5D3+4D4+3D5+2D6.
# If there is one letter, i.e.
# LD1D2D3D4D5D6. The sum is s=9*36+8L+7D1+6D2+5D3+4D4+3D5+2D6.
# The check digit c shall be the smallest non-negative integer such that s+c≡0 (mod 11).
# If c is 10, A is used instead.
# Write a program to calculate the check digit.
# '''
#
# converts = {
#     #Start Lowercases
#     'a':10,
#     'b':11,
#     'c':12,
#     'd':13,
#     'e':14,
#     'f':15,
#     'g':16,
#     'h':17,
#     'i':18,
#     'j':19,
#     'k':20,
#     'l':21,
#     'm':22,
#     'n':23,
#     'o':24,
#     'p':25,
#     'q':26,
#     'r':27,
#     's':28,
#     't':29,
#     'u':30,
#     'v':31,
#     'w':32,
#     'x':33,
#     'y':34,
#     'z':35,
#     # Start Capitals
#     'A':10,
#     'B':11,
#     'C':12,
#     'D':13,
#     'E':14,
#     'F':15,
#     'G':16,
#     'H':17,
#     'I':18,
#     'J':19,
#     'K':20,
#     'L':21,
#     'M':22,
#     'N':23,
#     'O':24,
#     'P':25,
#     'Q':26,
#     'R':27,
#     'S':28,
#     'T':29,
#     'U':30,
#     'V':31,
#     'W':32,
#     'X':33,
#     'Y':34,
#     'Z':35
# }
#
# idnum = input()
# splitted = [c for c in idnum]
# res = ''
#
# if len(idnum) == 7:
#     # Scripts for One letter
#     cal = 0
#     count = 1
#     cal = 9 * 36
#     #print('{} => {}'.format(splitted[0],converts[splitted[0]]))
#     cal += 8*converts[splitted[0]]
#     for i in range(7,1,-1):
#         #print('Count:{}, i:{}'.format(count,i))
#         #print('{}*int(splitted[{}])'.format(i,count))
#         cal += i*int(splitted[count])
#         count += 1
#     #print('Cal={}'.format(cal))
#     cal = cal%11
#     cal = 11-cal
#     if cal == 10:
#         res = 'A'
#     else:
#         res = str(cal)
# elif len(idnum) == 8:
#     #scripts for 2 letters
#     #print('To Be finished')
#     # Me lazy lmao
#     cal = 9*converts[splitted[0]]
#     cal += 8*converts[splitted[1]]
#     cal += 7*int(splitted[2])
#     cal += 6*int(splitted[3])
#     cal += 5*int(splitted[4])
#     cal += 4*int(splitted[5])
#     cal += 3*int(splitted[6])
#     cal += 2*int(splitted[7])
#     cal = 11-(cal%11)
#     if cal == 10:
#         res = 'A'
#     else:
#         res = cal
# print('{}({})'.format(idnum,res))
