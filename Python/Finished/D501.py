#!/usr/bin/python3.5
# Heung Shing Bank (D501)

acc = open('../account.txt', 'r')
d = acc.read()
d = d.splitlines()
m = 0
for i in range(int(d[0])+1):
    if i != 0:
        m += int(d[i])

print(m)
