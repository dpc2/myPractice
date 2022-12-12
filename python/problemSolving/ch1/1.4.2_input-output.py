# 1.4.2 - Input/Output

userName = input('Please enter your name:\n')
print('Here\'s your name in all caps:', userName.upper())
print('Your name is:', len(userName), 'characters long.')
print('\n')

# Type conversion can be necessary
userRadius = input('Enter the radius of the circle: ')
radius = float(userRadius)
diameter = 2 * radius
print(diameter)
print('\n')

# String formatting