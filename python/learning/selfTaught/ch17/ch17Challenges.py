# Challenge 1

import re
from os.path import dirname, join

currentDir = dirname(__file__)
path = join(currentDir, "zen.txt")

with open(path) as list:
    contents = list.read()

print(contents)

myGrep = re.findall('Dutch', contents, re.MULTILINE)
print(myGrep)


# Challenge 2

string = 'Arizona 479, 501, 870, California 209, 213, 650'
myRegex = re.findall('[\d]', string)
print(myRegex)


# Challenge 3

sentence = 'The ghost that says boo haunts the loo.'

myRegex = re.findall('.oo', sentence)
print(myRegex)


