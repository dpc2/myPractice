#------------------------------------------------#
#               Chapter 8 - Modules              #
#------------------------------------------------#

import math
import random
import statistics
import keyword
import cubed

print('\n')
print(math.pow(2,3))
print(random.randint(0,100))
print('\n')

num = [''] * 10

for index, item in enumerate(num):
    num[index] = random.randint(1,101)

print(len(num))

print("Random {} item list, 1 to 100: \n{}".format(len(num),num))

print('The mean is: {}'.format(statistics.mean(num)))
print('The median is: {}'.format(statistics.median(num)))
print('The mode is: {}'.format(statistics.mode(num)))
print('\n')


# Check if a string is a Python keyword

print(keyword.iskeyword("for"))
print(keyword.iskeyword("futbol"))




