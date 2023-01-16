#------------------------------------------------#
#                   Algorithms                   #
#------------------------------------------------#

# Fizzbuzzzz

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


# Sequential Search

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


# Palindrome

def palindrome(word):
    word = word.lower()
    return word[::-1] == word

print(palindrome("Mother"))
print(palindrome("Atoyota"))



# Anagram