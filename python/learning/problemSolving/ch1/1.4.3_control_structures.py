#------------------------------------------------#
#           1.4.3 - Control Structures           #
#------------------------------------------------#

# Algorithms two important control structures:
# iteration and selection

# While loops

counter = 1

while counter <= 10:
    print('Hello, world')
    counter += 1
print()

# done needs to be False, and counter <= 10
# while counter <= 10 and not done:...

# For loops

for item in [1,2,3,4,5,6]:
    print(item)
print()


for item in range(11):
    print(item ** 2)
print()


word_list = ['cat', 'dog', 'rabbit']
letter_list = []

for word in word_list:
    for letter in word:
        if letter not in letter_list:
            letter_list.append(letter)
print(letter_list)


# if, ifelse statements

import math

n = int(input('Enter an integer:\n'))

if n < 0:
    print('Sorry, value is negative')
else:
    print(math.sqrt(n))
print()


score = int(input('Score:\n'))

if score >= 90:
    print('A')
else:
    if score >= 80:
        print('B')
    else:
        if score >= 70:
            print('C')
        else:
            if score >= 60:
                print('D')
            else:
                print('F')
print()


if n < 0:
    n = abs(n)
print(math.sqrt(n))


# List comprehension

# A list compr. allows us to easily create a list
# based on some processing or selection criteria.

sq_list = []

for x in range(1, 11):
    sq_list.append(x * x)

print(sq_list)

# With list comprehension, this can be reduced
# down to:

sq_list = [x * x for x in range(1,11)]
print(sq_list)

sq_list = [x * x for x in range(1,11) if x % 2 != 0]
print(sq_list)

char_list = [ch.upper() for ch in 'comprehension' if ch not in 'aeiou']
print(char_list)


# Self check

# Number 1:
word_list = ['cat', 'dog', 'rabbit']
letter_list = []

for word in word_list:
    for letter in word:
        if letter not in letter_list:
            letter_list.append(letter)
print(letter_list)


# Number 2:
word_list = ['cat', 'dog', 'rabbit']
letter_list = [char for entry in word_list for char in entry]
print(letter_list)
