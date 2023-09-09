#------------------------------------------------#
#            1.4.5 Defining Functions            #
#------------------------------------------------#

def square(n):
    return n ** 2

print(square(3))
print(square(square(3)))
print()


# Square root function

def square_root(n):
    # Initial guess is 1/2 * n
    root = n /2

    for k in range(20):
        root = (1/2) * (root + (n/root))
        print(root)
    return root

print(square_root(9))
print()
print(square_root(131072))


# Self check