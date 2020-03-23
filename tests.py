import time
import random
import os
print('Loading...')

a = open('tests.sh', 'w')
a.write('')
time.sleep(random.random())
print('Detecting Python Files...')
files = []
sh = '#!/bin/bash\n'
for i in os.listdir('Python'):
    if i[-3:] == '.py':
        print(i)
        files.append('./Python/' + i)

for i in os.listdir('Python/Finished'):
    if i[-3:] == '.py':
        print(i)
        files.append('./Python/Finished/' + i)

print('Adding Files...')
count = 0
for a in files:
    print('\rAdding File ({}) [{} of {}]'.format(a, count + 1, len(files)), end='')
    count += 1
    sh += 'echo "Building File({})... [{} of {}]({}% finished)"\n'.format(a, count, len(files),
                                                                          ((count) / len(files)) * 100)
    sh += 'python -S -m py_compile {}\n'.format(a)
    time.sleep(random.random() / 5)
sh += 'echo "Buils tests done. Thank you."'
a = open('tests.sh', 'w')
print("Writing File")
a.write(sh)
print('Process finished. Thanks for using.')
a.close()
exit(15)
