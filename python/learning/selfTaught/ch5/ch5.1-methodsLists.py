#----------------------------------------------------------------------------------#
#                           Ch. 5 - Containers
#----------------------------------------------------------------------------------#
#
#   Here we'll learn to store objects in containers, like lists, tubples, and
#   dictionaries. Containers are like filing cabinets: they keep your data organized
#
#
#---------------------------------------#
#               Methods
#---------------------------------------#
# Similar to functions, methods execute code and return a result. Unlike functions,
# you can also call a method on an object.

x = "Hello".upper()
#print(x)

y = "Hello".replace("o", "@")
#print(y)

#----------------------------------------
#               Lists
#----------------------------------------
# Lists are containers that store objects in a specific order. They are iterable and
# mutable

fruit = list()
#print(fruit)

#or...

fruit = []
#print(fruit)

fruit = ["Apple", "Orange", "Pear"]
fruit.append("Banana")
fruit.append("Peach")
#print(fruit)

random = []
random.append(True)
random.append(100)
random.append(1.1)
random.append("HelloWorld")
#print(random)

colors = ["blue", "green", "yellow"]
#print(colors[4])   # IndexError: list index out of range
#print(colors)
colors[2] = "red"
#print(colors)
item = colors.pop() # Remove last item in list
#print(item)
#print(colors)

test = []
#test1 = test.pop()  # IndexError: pop from empty list

colors1 = ["red", "orange", "yellow"]
colors2 = ["green", "blue", "purple"]
combine = colors1 + colors2
print(combine)

colors = ["blue", "green", "yellow"]
test = "green" in colors
#print(test)
colors = ["blue", "green", "yellow"]
test = "black" not in colors
#print(test)

length = len(colors)
#print(length)

# An example...

colors = ["purple",
          "orange",
          "green"]

guess = input("Guess a color: \n")

if guess in colors:
    print("You guessed correctly!")
else:
    print("Wrong! Try again.")
