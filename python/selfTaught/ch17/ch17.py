#------------------------------------------------#
#                Ch. 17 - RegExs                 #
#------------------------------------------------#

# Many programming languages and OSes support regular
# expressions, a "sequence of characters that define
# a search pattern."

import re

print('\n')
l = 'Beautiful code is better than ugly.'

matches = re.findall('Beautiful', l)
otherMatches = re.findall('beautiful', l, re.IGNORECASE)

print(matches)
print(otherMatches)
print('\n')


#------------------------------------------------#
#               Match Beginning/End              #
#------------------------------------------------#

from os.path import dirname, join

currentDir = dirname(__file__)
path = join(currentDir, "zen.txt")

with open(path) as list:
    contents = list.read()

print(contents)

myGrep = re.findall('^If', contents, re.MULTILINE)
myOtherGrep = re.findall('idea.$', contents, re.MULTILINE)

print(myGrep)
print(myOtherGrep)
print('\n')


#------------------------------------------------#
#             Match Multiple Characters          #
#------------------------------------------------#

# Putting [abc] in a regex matches to a, b, or c.

string = 'Two too.'

mySearch = re.findall('t[ow]o', string, re.IGNORECASE)
print(mySearch)


#------------------------------------------------#
#                   Match Digits                 #
#------------------------------------------------#

myLine = '123?34 hello?'

mySearch = re.findall('\d', myLine, re.IGNORECASE)
print(mySearch)


#------------------------------------------------#
#                    Non Greedy                  #
#------------------------------------------------#

example = '__one__ __two__ __three__'

found = re.findall('__.*__', example)
print(found)

found = re.findall('__.*?__', example)

for match in found:
    print(match)
print('\n')


#------------------------------------------------#
#                Playing Mad Libs                #
#------------------------------------------------#

text = ('\
Giraffes have aroused the curiosity of \
__PLURAL_NOUN__ since earliest times.\
The giraffe is the tallest of all living \
__PLURAL_NOUN__, but scientists are unable \
to explain how it got its long __BODY_PART__ .\
The giraffe\'s tremendous height, which \
might reach __NUMBER__ __PLURAL_NOUN__, \
comes from its legs and __BODY_PART__.\
')

def mad_libs(mls):
    """
    :param mls: String with parts
    the user should fill out,
    surrounded by double underscores.
    Underscores cannot be inside
    hint, so no __hint_hint__, only
    __hint__.
    """

    hints = re.findall('__.*?__', mls)
    
    if hints is not None:
        for word in hints:
            q = 'Enter a {}\n'.format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print('\n')
        mls = mls.replace('\n', '')
        print(mls)
    else:
        print('invalid mls')

mad_libs(text)
print('\n')


#------------------------------------------------#
#                    Escaping                    #
#------------------------------------------------#

line = "I love $"

search = re.findall('\$', line, re.IGNORECASE)
print(search)
