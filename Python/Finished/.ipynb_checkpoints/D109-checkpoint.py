'''Giving changes(D109)
You are a trainee of the Heung Shing Bank. You are learning how to process withdrawals. For the convenience of the customers, you should always use the minimum possible number of currencies. Write a program to assist you.
You are provided with infinitely many $1000, $500, $100, $50, $20 and $10 notes.
Use the minimum number of notes to produce the exact amount.
'''
avbn = [1000,500,100,50,20,10]
wm = input()
wt = int(wm)

for i in avbn:
    while wt >= i:
        print(i)
        wt -= i
#        print('WT = {}'.format(wt))