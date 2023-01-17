#------------------------------------------------#
#              Ch. 21 Data Structures            #
#------------------------------------------------#

# Data structure: a format used to store and
# organize information. Ex: lists, tuples,
# dictionaries, but also stacks and queues.

#------------------------------------------------#
#                     Stacks                     #
#------------------------------------------------#

# A LIFO (last in, first out) data structure, with
# pops and pushes.

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []


myStack = Stack()
print(myStack.is_empty())

myStack.push(5)
print(myStack.is_empty())

item = myStack.pop()
print(item)
print(myStack.is_empty())

for i in range (0,9):
    myStack.push(i)

print(myStack.peek())
print(myStack.size())
myStack.clear()
print(myStack.is_empty())
print('\n')



# Reversing a string with a stack

myMessage = "Hello, World!"

for chars in myMessage:
    myStack.push(chars)

reverse = ""

print(range(len(myStack.items)))

# for i in range(0,13):
for i in range(len(myStack.items)):
    print(myStack.items)
    reverse += myStack.pop()

print(reverse)
print('\n')



#------------------------------------------------#
#                     Queues                     #
#------------------------------------------------#

# A FIFO (first in, first out) data structure, with
# enqueues and dequeues.

class myQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        # insert each new item into the 0th index (leftmost)
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def simulate_line(self, till_show, max_time):
        pq = myQueue()
        tix_sold = []

        for i in range(100):
            pq.enqueue("person" + str(i))

        t_end = time.time() + till_show
        now = time.time()

        while now < t_end and not pq.is_empty():
            now = time.time()
            r = random.randint(0, max_time)
            time.sleep(r)
            person = pq.dequeue()
            print(person)
            tix_sold.append(person)

        return tix_sold

    

queue = myQueue()
print(queue.is_empty())

for i in range(10):
    queue.enqueue(i)

print(queue.size())
print(queue.items)

for i in range(10):
    print(queue.dequeue())

print()
print(queue.size())
print()



#------------------------------------------------#
#                   Ticket Cue                   #
#------------------------------------------------#

import time
import random

movieQueue = myQueue()
sold = movieQueue.simulate_line(5, 1)
print(sold)

