#------------------------------------------------#
#       2.2 - What is Algorithm Analysis?        #
#------------------------------------------------#

import time


def sum_of_n(n):
    start = time.time()

    mySum = 0
    for i in range(1, n+1):
        mySum = mySum + i
    
    end = time.time()

    return mySum, end - start

def sum_of_n_better(n):
    start = time.time()
    sum = (n * (n + 1)) / 2
    end = time.time()

    return (sum, end - start)
    
def foo(tom):
    fred = 0
    for bill in range(1, tom+1):
        barney = bill
        fred = fred + barney

    return fred


print(sum_of_n(10))
print(foo(10))


for i in range(5):
    print('Sum is %d required %10.7f seconds' % sum_of_n(10000))
print()

for i in range(5):
    print('Sum is %d required %10.7f seconds' % sum_of_n(1000000))


print('Sum is %d required %10.7f seconds' % sum_of_n_better(10000))
print('Sum is %d required %10.7f seconds' % sum_of_n_better(100000))
print('Sum is %d required %10.7f seconds' % sum_of_n_better(1000000))
print('Sum is %d required %10.7f seconds' % sum_of_n_better(10000000))
print('Sum is %d required %10.7f seconds' % sum_of_n_better(100000000))

