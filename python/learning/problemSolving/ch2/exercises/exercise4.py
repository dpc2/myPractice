import random

# myList = [i for i in random.randint(0,50)]
listLength = 10
myList = [random.randint(0,50) for i in range(listLength)]
print(myList)

def mySort(list):
    for i in range(len(list)-1):

        if list[i] > list[i+1]:
            oldValue = list[i+1]
            list[i+1] = list[i]
            list[i] = oldValue

mySort(myList)
print(myList)
