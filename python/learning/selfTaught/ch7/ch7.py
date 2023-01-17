#----------------------------------------------------------------------------------#
#                           Ch. 7 - Loops
#----------------------------------------------------------------------------------#

#---------------------------------------#
#               For-Loops               #
#---------------------------------------#

name = "Danny"
for character in name:
    print(character)

shows = ["Breaking Bad", "Fraiser", "Cheers"]
for show in shows:
    print(show)

comedies = ("Seinfeld", "Friends", "The Office")
for show in comedies:
    print(show)

characters = {"Jerry": "Seinfeld",
            "Joey": "Friends",
            "Jim": "The Office"}
for character in characters:
    print(character + characters[character])

# Using the for loop to change items in an iterable
i = 0
showsCopy = shows
for show in showsCopy:
    new = showsCopy[i]
    new = new.upper()
    showsCopy[i] = new
    i += 1
print(showsCopy)

for item, show in enumerate(shows):
    show = show.upper()
print(shows)

# Using the for loop to move data between mutable iterables
drama = ["Grey's Anatomy", "The Sopranos", "Dawson's Creek"]
comedy = ["SNL", "South Park", "The Simpsons"]

allShows = []

for show in drama:
    show = show.upper()
    allShows.append(show)

for show in comedy:
    allShows.append(show.upper())

print(allShows)
print('\n')


#---------------------------------------#
#               Range                   #
#---------------------------------------#

for i in range(1, 11):
    print(i)


#---------------------------------------#
#            While-Loops                #
#---------------------------------------#

x = 10
while x > 0:
    print('{}'.format(x))
    x -= 1
print("Happy New Year!")

y = 1
while y <= 10:
    print('{}'.format(y))
    y += 1
print('Blast off!')
print('\n')

# Infinite loop
#while True:
    #print("This is the song that never ends...")

#---------------------------------------#
#               Break                   #
#---------------------------------------#

for i in range(0,100):
    print(i)
    break
print('\n')

# Infinite cycle of questions until q is entered
# n = (n+1) % 3 cycles from 0-2 repeatedly
questions = ["What is your name?\n",
            "What is your fave color?\n",
            "What is your quest?\n"]
n = 0
while True:
    print("Type q to quit")
    a = input(questions[n])
    if a == "q":
        break
    n = (n + 1) % 3
print('\n')

#---------------------------------------#
#               Continue                #
#---------------------------------------#

for i in range(1,6):
    if i == 3:
        continue
    print(i)
print('\n')

i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
print('\n')

#---------------------------------------#
#             Nested Loops              #
#---------------------------------------#

# For-loops in for-loops
for i in range(1,4):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)
print('\n')


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)
print(added)
print('\n')

# For-loop in while-loop, and vice versa
while input('y or n?') != 'n':
    for i in range(1,6):
        print(i)