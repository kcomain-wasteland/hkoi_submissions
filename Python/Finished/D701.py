'''Queue(D701)
Queue is a data structure that allows data to be accessed "First-in-first-out" efficiently. 
Specifically, it supports the following operations.

PUSH x: Insert x to the end of the queue.
FRONT: Returns the element at the front of the queue if there is any.
POP: Remove an element from the front of the queue if there is any.
SIZE: Returns the number of the elements in the queue currently.

In this exercise, we will implement a queue that handles integers.
'''

queue = []
ops = input()
for i in range(0,int(ops)):
    op = input()
    if op.split(' ')[0] == 'PUSH':
        queue.append(int(op.split(' ')[1]))
    elif op == 'SIZE':
        print(len(queue))
    elif op == 'POP':
        if len(queue) == 0:
            print('Cannot pop')
        else:
            queue.remove(queue[0])
    elif op == 'FRONT':
        if len(queue) == 0:
            print('Empty')
        else:
            print(queue[0])