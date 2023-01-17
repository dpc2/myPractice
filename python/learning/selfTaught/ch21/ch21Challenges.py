# Challenge 1

class MyStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return(len(self.items))

    def peek(self):
        lastItem = len(self.items) - 1
        return self.items[lastItem]

stackuary = MyStack()
myString = "yesterday"

for char in myString:
    stackuary.push(char)

for i in range(len(stackuary.items)):
    print(stackuary.pop())



# Challenge 2

myList = [1, 2, 3, 4, 5]
stackTastic = MyStack()

for i in myList:
    stackTastic.push(i)

reversed = []

for i in range(len(stackTastic.items)):
    reversed.append(stackTastic.pop())

print(reversed)

