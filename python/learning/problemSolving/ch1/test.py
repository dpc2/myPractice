import random

goal = "methinks it is like a weasel"


def generate():
    newString = ""
    global myRandDict 
    myRandDict = {'0':'a', '1':'b', '2':'c', '3':'d', '4':'e',
                    '5':'f', '6':'g', '7':'h', '8':'i', '9':'j',
                    '10':'k', '11':'l', '12':'m', '13':'n', '14':'o',
                    '15':'p', '16':'q', '17':'r', '18':'s', '19':'t',
                    '20':'u', '21':'v', '22':'w', '23':'x', '24':'y',
                    '25':'z', '26':' '}
    
    for i in range(len(goal)):
        newString = newString + myRandDict[str(random.randint(0,26))]

    return(newString)


myString = generate()
removeIndex = 14

print(myString)
print(myString[removeIndex])
print(myString[:len(myString)])
print(myString[1:len(myString)])
myNewString = myString[:removeIndex] + myString[removeIndex+1:len(myString)]
print(myNewString)