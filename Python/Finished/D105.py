'''Date comparison(D105)
Write a program to compare two dates: y1-m1-d1 y2-m2-d2
'''
a = input()
b = input()
ac = a.split(' ')
bc = b.split(' ')
if int(ac[0]) > int(bc[0]):
    print('After')
elif int(ac[0]) < int(bc[0]):
    print('Before')
elif int(ac[0]) == int(bc[0]):
    if int(ac[1]) > int(bc[1]):
        print('After')
    elif int(ac[1]) < int(bc[1]):
        print('Before')
    elif int(ac[1]) == int(bc[1]):
            if int(ac[2]) > int(bc[2]):
                print('After')
            elif int(ac[2]) < int(bc[2]):
                print('Before')
            elif int(ac[2]) == int(bc[2]):
                print('Same')

# print('AC:{}\nBC:{}'.format(ac,bc))