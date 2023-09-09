# Exercise #3: compare performance of del operator on
# lists + dictionaries

import random
import time

def test_del():
    for i in range(10000, 1000001, 20000):
        print(i)
        myDict = {j:None for j in range(i)}
        myList = [k for k in range(i)]

        time_start1 = time.time()
        # dictHalf = len(myDict)/2
        dictRand = random.randint(0,len(myDict))
        del myDict[dictRand]
        time_end1 = time.time()
        total_time1 = time_end1 - time_start1
        print('Dictionary del time: {}'.format(total_time1))
        print('Random dict object #: {}'.format(dictRand))
        print()

        time_start2 = time.time()
        # listHalf = int(len(myList)/2)
        listRand = random.randint(0,len(myList))
        del myList[listRand]
        time_end2 = time.time()
        total_time2 = time_end2 - time_start2
        print('List del time: {}'.format(total_time2))
        print('Random list object #: {}'.format(listRand))
        print()


test_del()


