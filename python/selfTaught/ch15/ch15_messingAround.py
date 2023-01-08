#------------------------------------------------#
#        Ch. 15 - Bringing It All Together       #
#------------------------------------------------#
import random

class Card:
    # index 0: spades, 1: hearts,
    # 2: diamonds, 3: clubs
    suits = ('spades','hearts',
            'diamonds','clubs')

    values = (None, None, '2', '3', '4',
                '5', '6', '7', '8', '9',
                '10', 'Jack', 'Queen',
                'King', 'Ace')

    def __init__(self, v, s):
        # suit and value are ints
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " \
            + self.suits[self.suit]
        return v


def randValue():
    return random.randint(2,14)

def randSuit():
    return random.randint(0,3)

def isEqual(card1, card2):
    return((card1.suit == card2.suit) and \
        (card1.value == card2.value))

#card1 = Card(randValue(), randSuite())
#card2 = Card(randValue(), randSuite())
#print(card1)
#print(card2)

#print(card1 > card2)
#print(card1 == card2)

count = 1
total = 0
loops = 10000
tries = []

while total < loops:
    card1 = Card(randValue(), randSuit())
    card2 = Card(randValue(), randSuit())

    if isEqual(card1, card2) == True:
        #print('Same? {}'.format(isEqual(card1, card2)))
        print('Card #1: {}\nCard #2: {}'.format(card1, card2))
        #print('It took: {} tries'.format(count))
        total += 1
        #print(count)
        tries.append(count)
        count = 1
        #break

    else:
        #print('Same? {}'.format(isEqual(card1, card2)))
        #print('Card #1: {}\nCard #2: {}'.format(card1, card2))
        #print('# of tries: {}'.format(count))
        #print('\n')
        count += 1

print(tries)
print('\n')

myTotal = 0

for entry in tries:
    myTotal += entry

print('Average tries: {}'.format(myTotal/len(tries)))

