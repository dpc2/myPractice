#------------------------------------------------#
#           2.2.2 - Anagram Detection            #
#------------------------------------------------#

#------------------------------------------------#
#                  Solution #1:                  #
#           Checking off each letter             #
#------------------------------------------------#

# Every position will be visited once before being found,
# so # of visits is 1 to n.

# (n(n+1))/2
# --> (1/2)*n^2 + (1/2)*n
# = O(n^2) as n gets large


def anagram_1(s1, s2):
    myList = list(s2)

    pos1 = 0
    still_OK = True

    while pos1 < len(s1) and still_OK:
        pos2 = 0
        found = False
        while pos2 < len(myList) and not found:
            if s1[pos1] == myList[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            myList[pos2] = None
        else:
            still_OK = False
        
        pos1 = pos1 + 1
    
    return still_OK

s1 = 'abcde'
s2 = 'edcba'
s3 = 'edca'

print('{} == {} ?\n{}'.format(s1, s2, anagram_1(s1, s2)))
print('{} == {} ?\n{}'.format(s1, s3, anagram_1(s1, s3)))
print()


#------------------------------------------------#
#                  Solution #2:                  #
#               Sort and Compare                 #
#------------------------------------------------#

# This algorithm is not O(n), even though there's only
# one simple iteration to compare n characters.

# The sort methods have their own cost, usually O(n^2)
# or O(n*log(n)). The sorting process dominates the
# Big-O value.


def anagram_2(s1, s2):
    list_1 = list(s1)
    list_2 = list(s2)

    list_1.sort()
    list_2.sort()

    position = 0
    matches = True

    while position < len(s1) and matches:
        if list_1[position] == list_2[position]:
            position += 1
        else:
            matches = False
        
    return matches


print('{} == {} ?\n{}'.format(s1, s2, anagram_2(s1, s2)))
print('{} == {} ?\n{}\n'.format(s1, s3, anagram_2(s1, s3)))



#------------------------------------------------#
#                  Solution #3:                  #
#                  Brute Force                   #
#------------------------------------------------#

# The brute force method is generating every combo of letters
# from s1 and seeing if s2 occurs. This results in: n! even
# if some combos are duplicates.

# For s1: 20 characters, there are 2.43 x 10^18 combinations
# One option every second would take 77 billion years to process



#------------------------------------------------#
#                  Solution #4:                  #
#               Count and Compare                #
#------------------------------------------------#

string1 = 'efshlkhsf'
string2 = 'oiaoyfjhl'
string3 = 'hkshfslef'

# First two iterations are not nested: 2n
# Third iteration always takes 26 steps
# O(n): 2n + 26

# This is achieved by sacrificing space (two lists
# for character counts)), a common tradeoff used to
# achieve speed.

def anagram_4(s1, s2):
    count1 = [0] * 26
    count2 = [0] * 26

    for i in range(len(s1)):
        # This uses the integers representing each letter
        # to fill out the lists.
        # position = 0 for a, 1 for b, 2 for c, etc...
        position = ord(s1[i]) - ord('a')
        count1[position] += 1

    for i in range(len(s2)):
        position = ord(s2[i]) - ord('a')
        count2[position] += 1

    j = 0
    still_OK = True

    while j < 26 and still_OK:
        if count1[j] == count2[j]:
            j += 1
        else:
            still_OK = False
        
    return still_OK

print('{} == {} ?\n{}'.format(string1, string2, anagram_4(string1, string2)))
print('{} == {} ?\n{}'.format(string1, string3, anagram_4(string1, string3)))
