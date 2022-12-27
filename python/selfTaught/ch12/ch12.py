#------------------------------------------------#
#        Ch. 12 - Programming Paradigms          #
#------------------------------------------------#

#------------------------------------------------#
#             Procedural Programming             #
#------------------------------------------------#

# Writing code to "do this, then that"

x = 2
y = 4
z = 8
xyz = x + y + z
print(xyz)
print('\n')

rock = []
country = []

def collectSongs():
    song = 'Enter a song:\n'
    ask = "\nType 'r' or 'c', or 'q' to quit:\n"

    while True:
        genre = input(ask)
        if genre == 'q':
            break
        if genre == 'r':
            rk = input(song)
            rock.append(rk)
        elif genre == 'c':
            ctry = input(song)
            country.append(ctry)
        
        else:
            print('Invalid input.\n')
    print(rock)
    print(country)

collectSongs()
print('\n')


#------------------------------------------------#
#            Functional Programming              #
#------------------------------------------------#

# "...is characterized by one thing: the abscence of
# side effects. It doesn't change or rely on data
# from outside the current function."

# A function with side effects:
a = 0

def increment():
    global a
    a += 1
 
 # A function with no side effects:

def increment(a):
    return a + 1


#------------------------------------------------#
#             Objective Programming              #
#------------------------------------------------#

class Orange:
    # __init__ executes when you create an Orange object
    # Two instance variables are created
    def __init__(self, w, c):
        """weights are in oz"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        self.mold = days * temp

orange1 = Orange(10, "blood orange")
orange2 = Orange(8, 'dark orange')
orange3 = Orange(14, 'yellow')
print('\n')

print('orange1: {}'.format(orange1))
print('orange1 weight: {}'.format(orange1.weight))
print('orange1 color: {}'.format(orange1.color))
print('\n')

# Reassigning object/instance variables
orange1.weight = 100
orange1.color = 'light orange'
print(orange1.weight)
print(orange1.color)
print('\n')

# Using rot function
newOrange = Orange(6, 'orange')
print(newOrange.mold)
newOrange.rot(10, 98)
print(newOrange.mold)
print('\n')


# Example 2
class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l

myRectangle = Rectangle(5, 4)
print('myRectangle: {} by {}\nArea: {}'.format(
    myRectangle.width, myRectangle.len, myRectangle.area()))
print(myRectangle.change_size(16, 9))
print('myRectangle: {} by {}\nArea: {}'.format(
    myRectangle.width, myRectangle.len, myRectangle.area()))