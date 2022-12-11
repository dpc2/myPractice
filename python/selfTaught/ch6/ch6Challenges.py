# Challenge 1

string = "Krampus"

for index, letter in enumerate(string):
    print(letter)


# Challenge 2

print("Yesterday I wrote a letter asking for {}. I sent it to {}!".format(
input("Enter your wishlist: "),
input("Enter name of the holiday gift giver: ")))


# Challenge 3

string = "aldous huxley was born in 1894."
print(string.capitalize())


# Challenge 4

string = "Who now? What now? Where now?"
print(string.split("?"))


# Challenge 5

list = ["A", "quick", "brown", "fox",
"jumps", "over", "the", "lazy", "dog", "."]

newList = list[0:-1]

print(" ".join(newList) + ".")


# Challenge 6 & 8

string = '"There must be some sort of way outta here" said the joker to the thief.\n'
string2 = '"There\'s too much confusion, I can\'t get no relief."'
string = string + string2
print(string.replace("s", "$"))


# Challenge 7

print("Hemingway".index("m"))


# Challenge 9

string = "three "
print(string + string + string)
print(string * 3)

# Challenge 10

string = "Twas the night before Xmas, and all through the house..."
print(string[:26])