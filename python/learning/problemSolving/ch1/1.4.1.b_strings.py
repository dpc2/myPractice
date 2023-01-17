# 1.4.1.b - Strings

print("Danny")
myName = "Danny"
print(myName[3])
print(myName * 2)
print(len(myName))

# Methods provided by strings
print(myName.upper())
print(myName.center(10))
print(myName.find('a'))
print(myName.split('a'))

# Lists vs strings - mutability
myList = [1,3,True,6.5]
print(myList)
myList[0] = 2**10
print(myList)
myName[0] = 'X'