# Challenge 1

import os

file = 'pythonRef.py'
path = os.path.join('/home','danny','documents',
                    'reference','code',file)

with open(path, 'r') as f:
    print(f.read())
print('\n')


# Challenge 2

with open('ch9#2.txt', 'w+') as f:
    f.write(input('What is your favorite color?:\n'))


# Challenge 3

import csv

myList = [['Aladdin', 'Hook', 'Mrs. Doubtfire',], ['Flubber',
            'The Birdcage', 'Dead Poets Society'], ['The Fisher King',
            'Jumanji', 'Patch Adams']]

with open('myCsv.csv', 'w') as f:
    myCsv = csv.writer(f, delimiter=',')
    for list in myList:
        myCsv.writerow(list)
