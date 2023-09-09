# Challenge 1
import random
import statistics

numArray = [''] * 10

for index, num in enumerate(numArray):
    numArray[index] = random.randint(1,101)

print(numArray)
print('\n')


# Challenge 2
import cubed

input = 10
print('{}^3 is:\n{}'.format(input,cubed.function(input)))

