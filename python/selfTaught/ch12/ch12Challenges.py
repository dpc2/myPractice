# Challenge 1

class Apples():
    def __init__(self, t, w, c, m):
        self.type = t
        self.weight = w
        self.color = c
        self.mold = m

    def rot(self, days, temp):
        if days >= 10 and temp >= 80:
            self.mold = True
        else:
            self.mold = False

apple1 = Apples('Granny Smith', 10, 'Ruby red', False)
print('\nMy apple:\nType: {}\nWeight: {}\nColor: {}\nMold: {}\n'
.format(apple1.type, apple1.weight, apple1.color, apple1.mold))

apple1.rot(10, 85)
print(apple1.mold)
print('\n')


# Challenge 2
import math

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        myArea = math.pi * self.radius ** 2
        return myArea

myCircle = Circle(5)

print('\nMy circle:\nRadius: {}\nArea: {:.2f}\n'.
format(myCircle.radius, myCircle.area()))

myCircle = Circle(10)

print('\nMy circle:\nRadius: {}\nArea: {:.2f}\n'.
format(myCircle.radius, myCircle.area()))



# Challenge 3

class Triangle():
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        myArea = 0.5 * self.base * self.height
        return myArea

myTriangle = Triangle(3, 3)

print('\nMy triangle:\nBase: {}\nHeight: {}\nArea: {}\n'.
format(myTriangle.base, myTriangle.height, myTriangle.area()))

myTriangle = Triangle(5, 4)

print('\nMy triangle:\nBase: {}\nHeight: {}\nArea: {}\n'.
format(myTriangle.base, myTriangle.height, myTriangle.area()))



# Challenge 4

class Hexagon():
    def __init__(self, s):
        self.side = s

    def perimeter(self):
        perm = self.side * 6
        return perm

myHexagon = Hexagon(3)

print('\nMy hexagon:\nSide: {}\nPerimeter: {}\n'.
format(myHexagon.side, myHexagon.perimeter()))

myHexagon = Hexagon(5)

print('\nMy hexagon:\nSide: {}\nPerimeter: {}\n'.
format(myHexagon.side, myHexagon.perimeter()))

