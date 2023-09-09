#----------------------------------------------------------------------------------#
#                           Ch. 6 - String Manipulation
#----------------------------------------------------------------------------------#

#  Here we will learn more about strings and go over some of Python's most useful
#  tools for manipulating them.


# Triple strings

myString = """
This is my
triple string
quote"""

print(myString + "\n")

#---------------------------------------#
#               Indexes
#---------------------------------------#

author = "Kafka"
for index, item in enumerate(author):
    print(item)
print("\n")

# String index out of range
#print(author[5])

# Negative indexes
print(author[-1])
print(author[-2])
print(author[-3])
print(author[-4])
print(author[-5])
print("\n")


#---------------------------------------#
#             Immutability
#---------------------------------------#

ff = "F. Fitzgerald"
print(ff[4])

# "Object does not support item assignment"
#ff[4] = "Z"


#---------------------------------------#
#            Concatenation
#---------------------------------------#

print("cat" + "in" + "hat")

#---------------------------------------#
#           String Manipulation         #
#---------------------------------------#

print("Tom Sawyer" * 3)

#---------------------------------------#
#       Change Case + Capitalize        #
#---------------------------------------#

print("Long ago, in a galaxy far far away...".upper())
print("ALL LOWER CASE".lower())
print("ob la di, ob la da".capitalize())

#---------------------------------------#
#               Format                  #
#---------------------------------------#

# Using the format method to replace {}
# brackets with the parameter passed in

last = "Shakespeare"
print("William {}".format(last))

author = "William Shakespeare"
birthYear = 1564
print("{} was born in {}.".format(author, birthYear))

# Inserting using responses into a string

noun1 = input("Enter a noun: ")
verb = input("Enter a verb: ")
adj = input("Enter an adjective: ")
noun2 = input("Enter another noun: ")

sentence = """
The {} {} the {} {}""".format(noun1, verb, adj, noun2)

print(sentence)

#---------------------------------------#
#               Split                   #
#---------------------------------------#

print("Hi!.Bye!".split("."))

#---------------------------------------#
#               Join                    #
#---------------------------------------#

firstThree = "abc"
result = "+".join(firstThree)
print(result)

sentence = ["A", "quick", "brown", "fox",
"jumps", "over", "the", "lazy", "dog"]
print("".join(sentence))
print(" ".join(sentence))

#---------------------------------------#
#              Strip Space              #
#---------------------------------------#

x = "           Hello              "
print(x.strip())

#---------------------------------------#
#               Replace                 #
#---------------------------------------#

sentence = "Not all that glitters is gold."
new = sentence.replace("t", "7")
print(new)

#---------------------------------------#
#            Find an index              #
#---------------------------------------#

print("Mississippi".index("i"))

# Error: substring not found
#print("XYZ".index("A"))

# Exception handling
try:
    print("animals".index("x"))
except:
    print("Not found.")


#---------------------------------------#
#                 In                    #
#---------------------------------------#

print("Cat" in "Cat in Hat")
print("Bat" in "Cat in Hat")
print("Potter" not in "Harry Potter")

#---------------------------------------#
#           Escaping Strings            #
#---------------------------------------#

# This will not work, cant do double inside double

#print("She said, "I know what it's like to be dead"")
print("She said, \"I know what it's like to be dead\"")

# Single quotes inside double are okay,
# as well as double within single quotes
print("She said, 'I know what it is to be sad.'")
print('She said, "You don\'t understand what I said"')

#---------------------------------------#
#               New line                #
#---------------------------------------#

print("line 1\nline 2\nline 3\n")

#---------------------------------------#
#               Slicing                 #
#---------------------------------------#

# Returns an iterable as a subset of another

authors = ["Tolstoy", "Huxley", "Orwell",
            "Falkner", "Steinbeck", "Dickins"]
# [0:3] returns items 0-2
print(authors[0:3])

x = "It's always darkest before the dawn"
# 0 and end are implied
print(x[:19])
print(x[20:])
print(x[:])