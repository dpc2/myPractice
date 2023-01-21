#------------------------------------------------#
#      1.4.6 - Object-Oriented Programming       #
#          in Python: Defining Classes           #
#------------------------------------------------#

# In OOP, classes can be considered an abstract data type.
# That way we can provide a logical description of what a
# data object looks like (its state) and what it can do
# (its methods).


#------------------------------------------------#
#                A Fraction Class                #
#------------------------------------------------#


class Fraction:
    
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print(self.num, '/', self.den)

    # Overriding __str__ method
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, f2):
        new_num = self.num * f2.den + f2.num * self.den
        new_den = self.den * f2.den
        common = gcd(new_num, new_den)
        # // forces int instead of float
        return Fraction(new_num // common, new_den // common)

    def __eq__(self, f2):
        first_num = self.num * f2.den
        second_num = f2.num * self.den

        return first_num == second_num


# Helper GCD function
def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n



myFraction = Fraction(3,5)
print(myFraction)


# 'show' method allows the Fraction object to print itself as a string
myFraction.show()


print("Damn, I ate", myFraction, "of the pizza, sorry guys.")
print(myFraction.__str__())
print(str(myFraction))
print(type(myFraction.__str__()))
print('\n\n')


# Adding Fraction objects
f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
print(gcd(48, 18))

print(f1 + f2)








