#------------------------------------------------#
#                Ch. 17 - RegExs                 #
#------------------------------------------------#

grep Beautiful zen.txt

# Ignore case
grep -i beautiful zen.txt

# Only print exact match
grep -o Beautiful zen.txt


#------------------------------------------------#
#               Match Beginning/End              #
#------------------------------------------------#

# Match beginning
grep ^If zen.txt
echo ""

# Match end
grep idea.$ zen.txt
echo ""


#------------------------------------------------#
#             Match Multiple Characters          #
#------------------------------------------------#

# Putting [abc] in a regex matches to a, b, or c.

echo Two too. | grep -i t[ow]o
echo ""

 
#------------------------------------------------#
#                   Match Digits                 #
#------------------------------------------------#

echo 123 hi 34 hello. | grep [[:digit:]]
echo ""


#------------------------------------------------#
#                    Reptition                   #
#------------------------------------------------#

echo two twoo twooo not too. | grep -o two*

# Following a period with asterisk, .*, matches any character
# zero or more times. Use it to match everything between two
# characters.

echo __hello__there | grep -o __.*__

# Asterisks are 'greedy'
echo __hello__there__my__friend | grep -o __.*__

# But they can be made 'ungreedy' in Python using ?


#------------------------------------------------#
#                     Escaping                   #
#------------------------------------------------#

echo I love $ | grep \$