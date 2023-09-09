def square():
    x = input("enter a number: \n")
    x = int(x)
    return x ** 2

#print(square())

#-------------------

def string():
    x = input("Enter a string, pls: \n")
    print(x)

#string()


#-------------------

def example(x, y, z, a = 1, b = 2):
    result = a + b + x + y + z
    return result

result = example(1, 2, 3)
#print(result)


#-------------------

def fun1():
    x = input("Enter a number: \n")
    x = int(x)
    return x / 2

#y = fun1()

def fun2():
    return y * 4

#z = fun2()
#print(z)



#-----------------

def last():
    x = input("Enter a string: \n")
    try:
        x = float(x)
        print(x)
    except ValueError:
        print("Can't convert to float if it's not a number.")

last()
