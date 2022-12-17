# Part 1

from os.path import dirname, join

currentDir = dirname(__file__)
path = join(currentDir, "input.txt")

with open(path) as list:
    contents = list.read().split("\n")

masterList = []
tempList = []
finalList = []

for i in contents:
    if i != '':
        tempList.append(i)
    else:
        masterList.append(tempList)
        tempList = []

highest = 0
secHighest = 0
thirdHighest = 0

for j, subList in enumerate(masterList):
    total = 0
    item = masterList[j]
    for k in item:
        calories = int(k)
        total += calories
    if highest < total:
        highest = total
    if highest > secHighest:
        secHighest = total
    if secHighest > thirdHighest:
        thirdHighest = total

print(highest)

# Part 2

