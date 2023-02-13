# Exercise #1: verify list index operator is O(1)
import random
import time

def experiment():

    myList = [0] * 1000000

    for index, item in enumerate(myList):
        myList[index] = random.randrange(1,100)

    print(myList)

    time_start = time.time()
    print(myList.index(50))
    time_stop = time.time()

    return(time_stop - time_start)

total = 0
runs = 50

for i in range(runs):
    result = experiment()
    total += result

average = total/runs
print(average)
