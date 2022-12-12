# 1.4.1.d - Sets

print({3,6,"Nugget",4.5,True})
mySet = {3,6,"Nugget",4.5,True}
print(mySet)

# Operations on a set
print(len(mySet))
print(True in mySet)
print("Mochi" in mySet)

# Methods on a set
mySet = {False, 3, 4.5, 6, 'Nugget'}
yourSet = {99, 3, 100}

print(mySet.union(yourSet))
print(mySet | yourSet)
print(mySet.intersection(yourSet))
print(mySet & yourSet)
print(mySet.difference(yourSet))
print(mySet - yourSet)
print(mySet.issubset(yourSet))
print({3,100} <= yourSet)
mySet.add("house")
print(mySet)
mySet.remove(4.5)
print(mySet)
mySet.pop()
print(mySet)
mySet.clear()
print(mySet)