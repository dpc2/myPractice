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


