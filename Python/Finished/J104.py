#!/usr/bin/python3.5


# Helper functions
def genstr(ln: int, chars: int):
    temp = []
    count = ln**2
    for i in range(chars):
        temp.append(str(count))
        count += ln

    return " ".join(temp)


# Real deal
c = int(input())
for p in range(c):
    print(genstr(p+1, c))
