#------------------------------------------------#
#               1.4.6 - Self Check               #
#------------------------------------------------#


class Fraction:
    
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print(self.num, '/', self.den)

    # Overriding built in magic methods
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, f2):
        new_num = self.num * f2.den + f2.num * self.den
        new_den = self.den * f2.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __sub__(self, f2):
        new_num = self.num * f2.den - f2.num * self.den
        new_den = self.den * f2.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __mul__(self, f2):
        new_num = self.num * f2.num
        new_den = self.den * f2.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __truediv__(self, f2):
        new_num = self.num * f2.den
        new_den = self.den * f2.num
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __gt__(self, f2):
        new_num1 = self.num * f2.den
        new_den = self.den * f2.den
        new_num2 = f2.num * self.den     
        return ((new_num1/new_den) > (new_num2/new_den))
        
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


# Math with Fraction objects
f1 = Fraction(3, 4)
f2 = Fraction(2, 3)
print(gcd(48, 18))
print()

#help(int)
print('{} plus {} equals {}'.format(f1, f2, f1 + f2))
print('{} minus {} equals {}'.format(f1, f2, f1 - f2))
print('{} times {} equals {}'.format(f1, f2, f1 * f2))
print('{} divided by {} equals {}'.format(f1, f2, f1 / f2))
print('{} > {} ?\n{}'.format(f1, f2, f1 > f2))
print('{} < {} ?\n{}'.format(f1, f2, f1 < f2))
