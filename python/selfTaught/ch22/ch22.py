#------------------------------------------------#
#                   Algorithms                   #
#------------------------------------------------#

#------------------------------------------------#
#                    Fizzbuzz                    #
#------------------------------------------------#

def myFizzbuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print('Fizzbuzz!')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

myFizzbuzz()
print()


#------------------------------------------------#
#                Sequential Search               #
#------------------------------------------------#

# A search algorithm finds information in a
# data structure like a list.

# A sequential search is a simple search
# algorithm that checks each item in a data
# structure to see if the item matches.

def seqSearch(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found

numbers = range(1,101)

search1 = seqSearch(numbers, 101)
print(search1)
search2 = seqSearch(numbers, 99)
print(search2)
print()


#------------------------------------------------#
#                   Palindrome                   #
#------------------------------------------------#

def palindrome(word):
    word = word.lower()
    return word[::-1] == word

print(palindrome("Mother"))
print(palindrome("Atoyota"))
print()



#------------------------------------------------#
#                    Anagram                     #
#------------------------------------------------#

def anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)

print(anagram('iceman', 'cinema'))
print(anagram('leaf', 'tree'))
print()



#------------------------------------------------#
#                 Count characters               #
#------------------------------------------------#

def count_characters(string):
    count_dict = {}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else: count_dict[c] = 1
    print(count_dict)

count_characters('Dynasty')



#------------------------------------------------#
#                    Recursion                   #
#------------------------------------------------#

# Recursion is solving problems by breaking them up
# into smaller problems that are more easily solved.

# So far we've used iterative algorithms, repeating
# steps over and over using a loop.
# Recursive algorithms rely on functions that call
# themselves, which can be a more elegant solution.

# A recursive algorithm is defined inside of a function.
# The function must have a base case, a condition to
# stop it from continuing forever.

# Each time the function calls itself, it moves closer
# to the base case, which is eventually satisfied and
# the function stops calling itself.

# 3 laws of recursion:
# - Recursive algorithm must have a base case
# - It must change its state and move closer to the
#   base case
# - It must call itself, recursively.


def bottles_of_beer(bob):
    """ Prints 99 Bottles of Beer
    on the Wall lyrics.
    :param bob: Must be a positive
    integer    
    """
    if bob < 1:
        print("No more bottles of beer on the wall. "
        "No more bottles of beer.")
        return
    tmp = bob
    bob -= 1
    print("{} bottles of beer on the wall, "
    "{} bottles of beer, you take one down, "
    "pass it around, {} bottles of beer on the "
    "wall.".format(tmp, tmp, bob))
    bottles_of_beer(bob)

bottles_of_beer(99)
