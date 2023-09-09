def even_odd():
    n = input("Type a number, any number: \n")
    n = int(n)
    if n % 2 == 0:
        print("n is even")
    else:
        print("n is odd")

#even_odd()
#even_odd()
#even_odd()


# Required and Optional Parameters

def f(x=2):
    return x**x

#print(f())
#print(f(4))


def add_it(x, y=10):
    return x + y

result = add_it(2)
#print(result)



# Global/local variables

def f():
    x = 1
    y = 2
    z = 3
    print(x)
    print(y)
    print(z)

#f()


x = 100

def f():
    global x
    x += 1
    print(x)

#f()


# Exception handling



try:
    a = input("type a number: \n")
    b = input("type another number: \n")
    a = int(a)
    b = int(b)
    print(a/b)
except (ZeroDivisionError, ValueError):
    print("Try again, dummy")

    

# Defining a variable within a try statement and using it in an
# except statement can mean the variable is never defined

try:
    10 / 0
    c = "I will never be defined :("
except ZeroDivisionError:
    print(c)



# Docstrings

def add(x, y):
    """
    Returns x + y.
    :param x: int
    :param y: int
    :return: int sum of x and y
    """

    return x + y
