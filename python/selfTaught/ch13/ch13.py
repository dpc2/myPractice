#------------------------------------------------#
#           Ch. 13 - Four Pillars of OOP         #
#------------------------------------------------#

#------------------------------------------------#
#                 Encapsulation                  #
#------------------------------------------------#

# Concept #1: In OOP, objects group variables (state),
# and methods (for altering/using state) in a single
# unit: the object.

class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

# len and width hold the object's state, which is grouped
# in the same unit as the 'area' method. The method uses
# the object's state to return the area.

# Concept #2: Encapsulation also refers to hiding the 
# class' internal data to prevent outside code from directly
# accessing it.

class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n

dataOne = Data()
print(dataOne.nums)
dataOne.nums[0] = 100
print(dataOne.nums)

dataOne.change_data(1,200)
print(dataOne.nums)


# Another example of encapsulation: private variables and
# methods. They hide a class's internal data to prevent
# the client from directly accessing it.

# Python resorts to naming convention to distinguish private
# variables and methods.

class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsanfe = "unsafe"

    def public_method(self):
        # clients can use this
        pass

    def _unsafeMethod(self):
        # clients shouldn't use this
        pass
    print('\n')



#------------------------------------------------#
#                 Abstraction                    #
#------------------------------------------------#

# "Taking away or removing characteristics from something
# in order to reduce it to a set of essential
# characteristics." Abstraction is used in OOP when
# you model objects using classes and omit unncessary
# details.



#------------------------------------------------#
#                Polymorphism                    #
#------------------------------------------------#

# "The ability to present the same interface for differing
# underlying forms (data types)." Interface = function or
# method.

print('Hello, World!')
print(200)
print(200.1)

print(type('Hello, World!'))
print(type(200))
print(type(200.1))

# The same interface (print) was presented for all 3 data
# types. No separate functions for print_int, etc...


# Drawing shapes, with/without polymorphism
# Without polymorphism:

class Shapes():
    def __init__(self, shp):
        self.shape = shp

    def draw(self):
        print('Draw {}!'.format(self.shape))

shapes = ['tr1', 'sq1', 'cr1']
myShapes = Shapes(shapes)
myShapes.draw()

for shape in shapes:
    if type(shape) == 'Triangle':
        shape.draw_Triangle()
    if type(shape) == 'Square':
        shape.draw_Square()
    if type(shape) == 'Circle':
        shape.draw_Circle()
print('\n')

# With polymorphism:
#for shape in shapes:
    #shape.draw()



#------------------------------------------------#
#                 Inheritance                    #
#------------------------------------------------#

# Similar to genetic inheritance, classes can inherit
# methods and variables from other classes.

class Shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} by {}""".format
        (self.width, self.len))

myShape = Shape(20, 25)
myShape.print_size()


class Square(Shape):
    def my_area(self):
        return self.width * self.width

    # Overriding print_size()
    def print_size(self):
        print("""I am {} by {}""".format
        (self.width, self.len))

mySquare = Square(20, 20)
mySquare.print_size()
print(mySquare.my_area())



#------------------------------------------------#
#                 Composition                    #
#------------------------------------------------#

# Composition models the "___ has a ___" relationship
# by storing an object as a variable in another object.

class Dog():
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person():
    def __init__(self, name):
        self.name = name

maddi = Person('Maddi')
tater = Dog('Tater', 'Good Boi', maddi)
print(tater.owner.name)

