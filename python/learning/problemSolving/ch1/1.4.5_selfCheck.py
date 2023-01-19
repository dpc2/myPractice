#------------------------------------------------#
#      1.4.5 Self Check - Monkeys in a Room      #
#------------------------------------------------#

import random

goal = "a long time ago in a galaxy far far away"

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


def compare(goal, attempt):
    score = 0

    for i, letter  in enumerate(goal):
        if letter != attempt[i]:
            break
        else:
            score += 1
    return(score)


def newCompare(goal, attempt):
    score = 0
    newBest = attempt
    tempLetter = ''
    print(newBest)
    print()

    for i, letter in enumerate(goal):
        while newBest[i] != letter:
            print("Letter to match: {}".format(letter))
            tempLetter = myRandDict[str(random.randint(0,26))]
            score += 1
            print(score)
            print('New random letter: {}'.format(tempLetter))

            if tempLetter == letter:
                tempString = newBest[:i] + tempLetter + newBest[i+1:len(newBest)]
                print(tempString)
                newBest = tempString
    print(newBest)
    return(score)

            
def runMonkeys():
    tally = 0
    highScore = 0
    bestString = ''

    while highScore != len(goal):
        newMaterial = generate()
        score = compare(goal,newMaterial)

        if score > highScore:
            highScore = score
            bestString = newMaterial

        if tally % 1000 == 0:
            print(highScore)
            print(bestString)
            print(tally)
        tally += 1



guess = generate()

newCompare(goal, guess)


