#------------------------------------------------#
#             Ch. 10 - Bringing It               #
#                 All Together                   #
#------------------------------------------------#

#------------------------------------------------#
#                   Hangman                      #
#------------------------------------------------#

import random

def hangman(word):
    wrong = 0
    stages = ["",
             "________         ",
             "|       |        ",
             "|       0        ",
             "|      /|\       ",
             "|      / \       ",
             "|                ",
             "|==============  "]
    rLetters = list(word)
    print(rLetters)
    board = ['__'] * len(word)
    win = False
    print('Welcome to Hangman!')
             
             
    while wrong < len(stages) - 1:
        print('\n')
        msg = 'Guess a letter\n'
        char = input(msg)
        if char in rLetters:
            cind = rLetters.index(char)
            board[cind] = char
            rLetters[cind] = '$'
        else:
            wrong += 1
        print((' '.join(board)))
        e = wrong + 1
        print('\n'.join(stages[0: e]))
        if '__' not in board:
            print('You win!')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong]))
        print('You lose! It was {}.'.format(word))

randomWords = ['hula hoop', 'elephant', 'zeppelin',
          'mason jar', 'lava lamp', 'text book',
          'fire wood', 'batman', 'squish mallow']

#randomIndex = random.randint(0,8)
#randomInput = randomWords[randomIndex]

hangman(randomWords[random.randint(0,8)])