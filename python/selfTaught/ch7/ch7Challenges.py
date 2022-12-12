#------------#
#     #1     #
#------------#

list = ["Avatar: The Last Air Bender", "JoJo's Bizarre Adventure",
        "Dragon Ball", "Cowboy Bebop"]

for show in list:
    print(show)
print('\n')


#------------#
#     #2     #
#------------#

i = 25
while i <= 50:
    print(i)
    i += 1
print('\n')


#------------#
#     #3     #
#------------#

for show in list:
    print("{}\t{}".format(list.index(show),show))
print('\n')


#------------#
#     #4     #
#------------#

list = [0, -1000, 10, 1969, 666]

while True:
    answer = input("Guess a number: \n")
    if answer == 'q':
        break
    else:
        answer = int(answer)
        if answer in list:
            print("You guessed correctly!\n")
        else:
            print("Guess again\n")
print('\n')


#------------#
#     #5     #
#------------#

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
newList = []

for i in list1:
    for j in list2:
        newList.append(i * j)
print(newList)
print('\n')




