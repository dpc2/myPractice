#------------------------------------------------#
#                 2.3.1 - Lists                  #
#------------------------------------------------#

# Lists were designed with the most commonly used operations
# highly optimized, while less common ones sometimes have a
# performance tradeoff.

# Two common operations: indexing and assigning to an index
# position. These operations are independent of the list
# size, making them O(1).

# Another common operations: growing a list.
# Appending is O(1), concatenating is O(k), where k is the
# size of the list that is being concatenated.


# Example: 4 ways to generate a list of n numbers.


# Number 1: concatenation

def test1():
    myList = []
    for i in range(1000):
        myList = myList + [i]


# Number 2: append

def test2():
    myList = []
    for i in range(1000):
        myList.append(i)


# Number 3: list comprehension

def test3():
    myList = [i for i in range(1000)]


# Number 4: The "Oh, duh" method

def test4():
    myList = list(range(1000))


def test5():
    return    


# timeit will be used to compare methods. timeit runs functions
# in a consistent environment using timing mechanisms that are
# as similar as possible across operating systems.

import timeit
from timeit import Timer

t1 = Timer('test1()', 'from __main__ import test1')
print('Test #1: concatenation ', t1.timeit(number=1000), 'milliseconds')

t2 = Timer('test2()', 'from __main__ import test2')
print('Test #2: append ', t2.timeit(number=1000), 'milliseconds')

t3 = Timer('test3()', 'from __main__ import test3')
print('Test #3: comprehension ', t3.timeit(number=1000), 'milliseconds')

t4 = Timer('test4()', 'from __main__ import test4')
print('Test #4: "duh" method ', t4.timeit(number=1000), 'milliseconds')

t5 = Timer('test5()', 'from __main__ import test5')
print('Test #5: empty function ', t5.timeit(number=1000), 'milliseconds')


#------------------------------------------------#
#                pop() from list                 #
#------------------------------------------------#

# pop() has two difference Big-O times associated with it, depending
# on whether you're popping the end of the list (O(1)) or elsewhere
# (O(n)).

# x.pop...import x is used to we can still use our list object and
# just have the single pop statements


pop_zero = Timer('x.pop(0)', 'from __main__ import x')
pop_end = Timer('x.pop()', 'from __main__ import x')

x = list(range(2000000))
print(pop_zero.timeit(number=1000))

x = list(range(2000000))
print(pop_end.timeit(number=1000))



# Testing over a range of list sizes

print('pop(0) pop()')
for i in range (1000000, 100000001, 1000000):
    x = list(range(i))
    p1 = pop_end.timeit(number=1000)
    x = list(range(i))
    p2 = pop_zero.timeit(number=1000)
    print("%15.5f, %15.5f" % (p2, p1))

