#------------------------------------------------#
#                  Ch. 9 - Files                 #
#------------------------------------------------#

#------------------------------------------------#
#                Writing to Files                #
#------------------------------------------------#

# You shouldn't write file paths yourself, instead
# build them with 'os' module function 'path', to
# be OS agnostic

import os

path = os.path.join('home',
                    'danny',
                    'code',
                    'python',
                    'selfTaught',
                    'ch9')
print(path)

# Open function can run in several modes
# r - read only
# w - write only
# w+ - read/write, overwriters existing file
# or creates it if it didn't exist

testFile = open('test.txt', 'w')
testFile.write('Hello from Python!')
testFile.close()


#------------------------------------------------#
#          Automatically Closing Files           #
#------------------------------------------------#

# To avoid having to close files, use a 'with'
# statement: a compound statement with an action
# that occurs when Python leaves it.

# The file object is named 'f'
with open('test2.txt', 'w') as f:
    f.write('Hullo there, from Python!\n')


#------------------------------------------------#
#               Reading from Files               #
#------------------------------------------------#

myList = list()

with open('test2.txt', 'r') as f:
    file = f.read()
    myList.append(file)
    print(file)

    for index, letter in enumerate(file):
        print('{}: {}'.format(index,letter))


print(myList)
print('\n')


#------------------------------------------------#
#                   CSV Files                    #
#------------------------------------------------#

import csv

with open('test.csv', 'w', newline='') as f:
    w = csv.writer(f, delimiter=',')
    w.writerow(['seven','eight','nine'])
    w.writerow(['ten','eleven','twelve'])

with open('test.csv', 'r') as f:
    myCsv = csv.reader(f, delimiter=',')
    for row in myCsv:
        print(row)
        print(','.join(row))

