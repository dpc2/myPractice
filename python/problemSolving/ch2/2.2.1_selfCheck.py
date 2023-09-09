#------------------------------------------------#
#               2.2.1 - Self Check               #
#------------------------------------------------#

import random

myList = []

for i in range(int(input("Enter n:\n"))):
 myList.append(random.randint(0,100))


# First function: O(n^2)
def Function1(list):
    currentMin = list[0]
    print(list)

    for i in list:
        for j in list:
            if i < currentMin:
                currentMin = i
            if j < currentMin:
                currentMin = j
    return currentMin


# Second function: O(n)
def Function2(list):
    currentMin = list[0]

    for i in list:
        if i < currentMin:
            currentMin = i
    return currentMin


print(Function1(myList))
print(Function2(myList))
