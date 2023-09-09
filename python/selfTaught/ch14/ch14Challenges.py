# Challenge 1

class Square:
    square_list = []

    def __init__(self, s):
        self.side = s
        self.square_list.append(self.side)
        print(self.square_list)

sq1 = Square(5)
sq2 = Square(10)
sq3 = Square(15)
print('\n')



# Challenge 2

class Square:

    def __init__(self, s):
        self.side = s

    def __repr__(self):
        return('{} by {} by {} by {}'.format
        (self.side, self.side, self.side, self.side))

sq1 = Square(5)
sq2 = Square(10)
print(sq1)
print(sq2)
print('\n')



# Challenge 3

class Fruit:
    def __init__(self, name):
        self.name = name


def myFunction(object1,object2):
    return(object1 is object2)

fruit1 = Fruit('strawberry')
fruit2 = fruit1
fruit3 = Fruit('banana')

print(myFunction(fruit1, fruit2))
print(myFunction(fruit1, fruit3))
