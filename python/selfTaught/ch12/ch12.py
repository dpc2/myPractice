#------------------------------------------------#
#        Ch. 12 - Programming Paradigms          #
#------------------------------------------------#

#------------------------------------------------#
#             Procedural Programming             #
#------------------------------------------------#

# Writing code to "do this, then that"

x = 2
y = 4
z = 8
xyz = x + y + z
print(xyz)
print('\n')

rock = []
country = []

def collectSongs():
    song = 'Enter a song:\n'
    ask = "\nType 'r' or 'c', or 'q' to quit:\n"

    while True:
        genre = input(ask)
        if genre == 'q':
            break
        if genre == 'r':
            rk = input(song)
            rock.append(rk)
        elif genre == 'c':
            ctry = input(song)
            country.append(ctry)
        
        else:
            print('Invalid input.\n')
    print(rock)
    print(country)

collectSongs()