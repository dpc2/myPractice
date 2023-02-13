# Exercise #2: verify 'get' and 'set' item for
# dictionaries is O(1).

import random
import time

def test_get():
    for i in range(10000, 1000001, 20000):
        myDict = {j:None for j in range(i)}
        myRand = random.randint(0,i)
        time_start = time.time()
        myGet = myDict.get(myRand)
        time_end = time.time()
        total_time = time_end - time_start
        print(i, myRand, total_time)

def test_set():
    for i in range(10000, 1000001, 20000):
        myDict = {j:None for j in range(i)}
        myRand = random.randint(0,i)
        time_start = time.time()
        myDict.update({myRand: None})
        time_end = time.time()
        total_time = time_end - time_start
        print(i, myRand, total_time)


test_get()
test_set()
