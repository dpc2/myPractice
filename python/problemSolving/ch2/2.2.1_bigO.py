#------------------------------------------------#
#              2.2.1 - Big-O Notation            #
#------------------------------------------------#

# Execution time can be expressed as the number of steps
# required to solve the problem. Deciding on a basic unit
# of computation can be complicated, it depends on the
# algorithm being implemented.

import time

# in sum_of_n(), counting the # of assign statements
# could be a good basic unit.

def sum_of_n(n):
    start = time.time()

    mySum = 0                       # 1 assign statement
    for i in range(1, n+1):
        mySum = mySum + i           # n assign statements
    
    end = time.time()

    return mySum, end - start


# T(n) = 1 + n
# n is the 'size of the problem', therefore 'T(n) is
# the time is takes to solve a problem of size n:
# 1 + n steps.


# Sometimes the size of the problem isn't as important
# as the exact values of the data. In these cases, we
# can characterize the performance is terms of:
# best case, worst case, and avg. case.

n = input("Enter n\n")

a = 5
b = 6
c = 10                          # 3 assign ops

for i in range(n):
    for j in range(n):
        x = i * j
        y = j * j
        z = i * j               # 3n^2 assign ops (nested loops)
for k in range(n):
    w = a * k + 45
    v = b * b                   # 2n assign ops
d = 33                          # 1 assign op

# Total = 3n^2 + 2n + 4
# --> O(n2), everything else drops away

