#-------------------------------#
#           Dictionaries
#-------------------------------#
# Dictionaries are used to link one object (a key) to another object (the value), in a
# process called "mapping". The result is a key-value pair. Keys can be looked up to
# get the corresponding value, but not the other way around. Objects are not stored in
# any specific order.

my_dict = dict()

# or...

my_dict = {}
print(my_dict)

fruits = {"Apple": "Red", "Banana": "Yellow"}
print(fruits)

facts = dict()

# add a value
facts["code"] = "fun"
# look up a key
# print(facts["code"])

facts["Bill"] = "Gates"
# print(facts["Bill"])

facts["founded"] = 1776
# print(facts["founded"])

for i in facts:
    print(facts[i])

question = "Bill" in facts
print(question)

# key-value pairs can be deleted with "del"
books = {"Dracula": "Stoker", "1984": "Orwell", "The Trial": "Kakfa"}
print(books)
del books["The Trial"]
print(books)

# Last example

rhymes = {"1": "fun",
        "2": "blue",
        "3": "me",
        "4": "floor",
        "5": "alive"
}

n = input("Type a number: ")
if n in rhymes:
        rhyme = rhymes[n]
        print(rhyme)
else:
        print("Not found")