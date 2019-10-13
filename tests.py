print('Loading...')
import time
import random
import os
time.sleep(random.random())
print('Detecting Python Files...')
files = []
sh = '#!/bin/bash\n'
for i in os.listdir('Python'):
    if i[-3:] == '.py':
        print(i)
        files.append('./Python/'+i)

for i in os.listdir('Python\\Finished'):
    if i[-3:] == '.py':
        print(i)
        files.append('./Python/Finished/'+i)

print('Please Wait... Adding Files.')
count = 0
for a in files:
    print('Adding File ({}) [{} of {}]'.format(a,count+1,len(files)))
    count += 1
    sh += 'echo "Building File({})... [{} of {}]({}% finished)"\n'.format(a,count,len(files),((count)/len(files))*100)
    sh += 'python -S -m py_compile {}\n'.format(a)
    time.sleep(random.random()/5)
a = open('tests.sh','w')
sh += 'echo "Buils tests done. Thank you."'
a.write(sh)
print('Process finished. Thanks for using.')
a.close()
exit(15)