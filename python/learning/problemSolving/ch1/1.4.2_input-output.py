#------------------------------------------------#
#              1.4.2 - Input/Output              #
#------------------------------------------------#

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


#------------------------------------------------#
#               String Formatting                #
#------------------------------------------------#

print('Hello')
print('Hello', 'World')
print('Hello', 'World', sep='***')
print('Hello', 'World', end='***')
print('Hello', end='***'); print('World')
print()


# Formatted strings

name = 'Danny'
age = 31

print(name, 'is', age, 'years old.')
print('%s is %d years old.' % (name, age))
print()

price = 24
item = 'banana'
print('The %s costs %d cents' % (item, price))
print('The %-10s costs %5.2f cents' % (item, price))
print('The %+10s costs %5.2f cents' % (item, price))
print('The %+10s costs %10.2f cents' % (item, price))
item_dict = {'item': 'banana', 'cost': 24}
print('The %(item)s costs %(cost)7.1f cents' % item_dict)
