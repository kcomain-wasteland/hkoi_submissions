#!/usr/bin/python3.5

# D402

# Setup variables

db = {}

# Set database items
dbitems = int(input())
for i in range(dbitems):
    item = input()
    item = item.split(' ')
    db[item[0]] = float(item[1])

# Get database and scan stuff
iceagebaby = int(input())
moni = 0
for i in range(iceagebaby):
    item2 = input()
    moni += db[item2]

print(float(round(moni, 1)))
