#------------------------------------------------#
#           1.4.4 - Exception Handling           #
#------------------------------------------------#

# Two types of errors: syntax errors and logic errors.
# Logic errors lead to runtime errors (exceptions)
# that cause the program to terminate.

import math

a_number = int(input('Please enter an integer:\n')) 
try:
    print(math.sqrt(a_number))
except:
    print('Bad value for square root')
    print('Using absolute value instead')
    print(math.sqrt(abs(a_number)))


# Creating our own RuntimeError
if a_number < 0:
    raise RuntimeError("You can't use a negative number.")
else:
    print(math.sqrt(a_number))



