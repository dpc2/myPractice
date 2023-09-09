# 1.4.1.a - Lists

myList = [0] * 6
print(myList)

myList = [1,2,3,4]
A = [myList] * 3
print(A)
myList[2] = 45
print(A)

# Methods provided by lists
myList = [1024, 3, True, 6.5]
myList.append(False)
print(myList)
myList.insert(2,4.5)
print(myList)
print(myList.pop())
print(myList)
print(myList.pop(1))
print(myList)
myList.pop(2)
print(myList)
myList.sort()
print(myList)
myList.reverse()
print(myList)
print(myList.count(6.5))
print(myList.index(4.5))
myList.remove(6.5)
print(myList)
del myList[0]
print(myList)

print((54).__add__(21))

# Use of range
print(range(10))
print(type(range(10)))
print(list(range(10)))
print(range(5,10))
print(list(range(5,10)))
print(list(range(5,10,2)))
print(list(range(10,1,-1)))
