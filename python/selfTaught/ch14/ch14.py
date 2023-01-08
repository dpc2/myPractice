#------------------------------------------------#
#                Ch. 14 - More OOP               #
#------------------------------------------------#

#------------------------------------------------#
#           Class vs Instance Variables          #
#------------------------------------------------#

# In Python, classes are objects. Each class is an
# object that is an instace of class "type".

class Square:
    pass

print(Square)
print(type(Square))
print('\n')

# Classes have class variables and instance variables.
# Everythings so far has been the latter, defined with
# 'self.thing = thing'. Instance variables belong to
# objects.

class Rectangle():
    rectangles = []

    def __init__(self, w, l):
        # Instance variables width and len
        self.width = w
        self.len = l
        # Class variable
        self.rectangles.append((self.width,self.len))
        #print(self.rectangles)
        
    def print_size(self):
        print("""{} by {}""".format
        (self.width, self.len))

r1 = Rectangle(20, 25)
r1.print_size()
print(type(r1.width))

r2 = Rectangle(30, 35)
r3 = Rectangle(40, 45)
print(Rectangle.rectangles)
print('\n')

# Class variables belong to the object Python creates for
# each class definition and they objects THEY create.
# Class variables allow us to share data between all class
# instances without relying on global variables.



#------------------------------------------------#
#                  Magic Methods                 #
#------------------------------------------------#

# Every class in Python inherits from a parent class called
# Object. Python utilizes the methods inherited from Object
# in different situations, like when printing an object.

class Lion:
    def __init__(self, name):
        self.name = name

    # Overriding __repr__
    def __repr__(self):
        return self.name

lion = Lion('Leo')
print(lion)
print('\n')


# Operands must have a magic method the operator (+,-,/,*,...)
# can use to evaluate expressions. In '2+2', each integer
# object has a magic method called __add__ that Python calls
# when evaluating the expression.

class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    # Overriding __add__ to return abs value
    def __add__(self, other):
        return (self.n + other.n)
        #return abs(self.n + other.n)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)
z = AlwaysPositive(-30)

print(type(x)) # <class '__main__.AlwaysPositive'>
print(type(x.n)) # <class 'int'>

# def __add__ is needed in class AlwaysPositive to be able to
# add alwaysPositive objects
print(x+y)
print(x+z)
print('\n')


#------------------------------------------------#
#                      Is                        #
#------------------------------------------------#

# 'is' returns True if two objects are the same, and
# False if they are not.

class Person:
    def __init__(self):
        self.name = 'Bob'

bob = Person()
sameAsBob = bob
#anotherBob = bob
anotherBob = Person()

# True
print(bob is sameAsBob)

# False, because bob and anotherBob refer to different objects
print(bob is anotherBob)


# Using 'if' to check if a variable is None:

def xCheck(x):
    if x is None:
        print('x is None :(')
    else:
        print('x is not None')

x = None
xCheck(x)

x = 10
xCheck(x)

