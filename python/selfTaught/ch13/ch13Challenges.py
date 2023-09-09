# Challenge 1 and 2

class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l
    def calc_perimeter(self):
        return 2 * self.width + 2 * self.len

class Square():
    def __init__(self, l):
        self.len = l
    def calc_perimeter(self):
        return 4 * self.len
    def change_size(self, d):
        self.diff = d
        self.len += self.diff


myRectangle = Rectangle(5, 6)
print('myRectangle has perimeter: {}\n'.format
(myRectangle.calc_perimeter()))

mySquare = Square(3)
print('mySquare has perimeter: {}\n'.format
(mySquare.calc_perimeter()))

mySquare.change_size(-1)
print('mySquare has perimeter: {}\n'.format
(mySquare.calc_perimeter()))



# Challenge 3

class Shape():
    def __init__(self):
        pass
    def what_am_i(self):
        print('I am a shape.\n')

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l
    def calc_perimeter(self):
        return 2 * self.width + 2 * self.len

class Square(Shape):
    def __init__(self, l):
        self.len = l
    def calc_perimeter(self):
        return 4 * self.len
    def change_size(self, d):
        self.diff = d
        self.len += self.diff


myRectangle = Rectangle(3,4)
print('myRectangle has perimeter: {}\n'.format
(myRectangle.calc_perimeter()))

mySquare = Square(5)
print('mySquare has perimeter: {}\n'.format
(mySquare.calc_perimeter()))

myRectangle.what_am_i()
mySquare.what_am_i()



# Challenge 4

class Horse():
    def __init__(self, breed, name, height, rider):
        self.breed = breed
        self.name = name
        self.height = height
        self.rider = rider

class Rider():
    def __init__(self, name):
        self.name = name

rider = Rider("myRider")
seaBiscuit = Horse("Colt", "Sea Biscuit", "5'2\"", rider)

print('Breed: {}'.format(seaBiscuit.breed))
print('Name: {}'.format(seaBiscuit.name))
print('Height: {}'.format(seaBiscuit.height))
print('Rider: {}'.format(seaBiscuit.rider.name))
