#------------------------------------
#               Tuples
#------------------------------------
# A container that stores objects in a specific order. They are immutable: no mods,
# additions, removals, etc. A comma is needed, even if there's only 1 object in the
# tuple. Tuples can also be used as keys in dictionaries, since they don't change.

my_tuple = tuple()

# or...

my_tuple = ()

random = ("M. Jackson", 1958, True)
print(random)

# This is a tuple:
("self_taught",)

# This is not a tuple:
(9) + 1

# Tuples are immutable, cannot be modified
dys = ("1984", "Brave New World", "Fahrenheit 451")
#dys[1] = "Handmaid's Tale"
question = "1984" in dys
question2 = "Handmaid's Tale" not in dys
print(question)
print(question2)