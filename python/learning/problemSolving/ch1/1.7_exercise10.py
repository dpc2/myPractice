#------------------------------------------------#
#              1.4.7 - Exercises 10              #
#------------------------------------------------#

import random


mySuites = {'hearts': 1, 'spades': 2, 'clubs': 3, 'diamonds': 4}
myValues = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5,
            '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
            'Jack': 11, 'Queen': 12, 'King': 13}



def deal(p):
    p.hand.append(gameDeck.myDeck.pop())


def giveCard(removeFrom, to, card): 
    removeFrom.hand.remove(card)
    to.hand.append(card)


def turn(x, y):
    lucky = False

    # pick card in own hand
    randomCard = x.hand[random.randrange(len(x.hand))]
    randomValue = randomCard.value
    print('Player {}: Do you have any {}s?'.format(x.name, randomValue))

    for i in y.hand:
        if randomValue in str(i):
            print('Player {}: Yes, I have {}'.format(y.name, i))
            print()
            lucky = True
            giveCard(y, x, i)
        if lucky == True:
            break
    if lucky == False:
        print('Go fish!')
        print()


def handStatus(p1, n):
    print('Player {} hand:\n'.format(n))
    for i in p1.hand:
        print(i)
    print()


def checkHands(p1, p2):
    tempList = []

    for i in p1.hand:
        #print(i.value)
        tempList.append('{} of {}'.format
        (i.value, i.suite))
        if sum(i.value in s for s in tempList) >= 2:
            layDown(p1, i.value)

    #print(tempList)
    print()


def layDown(player, val):

    tempList = []
    print('Cards of same value found!\n{}'.format(val))
    print()
    handStatus(player, 1)

    for i in player.hand:
        if i.value == val:
            tempList.append(i)
            player.hand.remove(i)
            player.table.append(tempList)
    handStatus(player, 1)
    
                



class cards():
    def __init__(self, s, v):
        self.suite = s
        self.value = v

    def __str__(self):
        return ('{} of {}'.format(self.value, self.suite))


class deck():
    def __init__(self):
        self.myDeck = []
        for s in mySuites:
            for v in myValues:
                self.myDeck.append(cards(s, v))
        random.shuffle(self.myDeck)

    def __str__(self):
        return('{}'.format(self.myDeck))
    
    def pop(self):
        self.myDeck.pop()


class player():
    def __init__(self, n):
        self.name = n
        self.hand = []
        self.table = []

    def checkHand(self):
        tempList = []

        for i in self.hand:
            print(i)
            myCount = self.hand.count(i.value)
            print(myCount)

gameDeck = deck()



def myGame():
    #player1 = player(input('Player 1 name:\n'))
    #player2 = player(input('Player 2 name:\n'))
    player1 = player('p1')
    player2 = player('p2')
    print()

    for i in range(5):
        deal(player1)
        deal(player2)
    handStatus(player1, player2)    
    
    turn(player1, player2)
    handStatus(player1, 1)
    handStatus(player2, 2)
    checkHands(player1, player2)


myGame()
