#------------------------------------------------#
#              2.3.2 - Dictionaries              #
#------------------------------------------------#

# The get() and set() dictionary operations are both O(1).
# Using 'contains' operatoins is also O(1).

# Here we'll compare performance of the 'contains' operation
# between lists and dictionaries. In the process we'll prove
# that 'contains' is O(n) for lists and O(1) for dicts.

# We will make a list with a range of numbrs, then pick
# numbers at random and check to see if the numbers are in
# the list. Bigger lists should take longer to determine.

# Dictionaries should prove to be consistent and much faster.

import timeit
import random

for i in range(10000, 1000001, 20000):
    t = timeit.Timer('random.randrange(%d) in x' % i,
                    'from __main__ import random,x')
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    d_time = t.timeit(number=1000)
    print('%d,%10.3f, %10.3f' % (i, lst_time, d_time))
