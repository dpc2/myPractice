#------------------------------------------------#
#              1.4.7 - Exercises 1-9             #
#------------------------------------------------#

class Fraction:
    def __init__(self, num, den):
        if type(num) != int or type(den) != int:
            print("Error: please enter an integer")
        else:     
            if den < 0:
                num = -num
                den = abs(den)
            self.gcd = GCD(num, den)
            self.num = num // self.gcd
            self.den = den // self.gcd

    def __str__(self):
        return (str(self.num) + "/"
        + str(self.den))

    def get_num(self):
        return str(self.num)

    def get_den(self):
        return str(self.den)

    def __add__(self, frac2):
        print('__add__ is working')
        if type(frac2) == float or type(frac2) == Fraction:
            new_num =  self.num * frac2.den + frac2.num * self.den
            new_den = self.den * frac2.den
        else:
            new_num = self.num + frac2 * self.den
            new_den = self.den
        return Fraction(new_num, new_den)
        
    __radd__ = __add__

    #def __iadd__(self, int):
        #new_num = self.num + int * self.den
        #new_den = self.den
        #return Fraction(new_num, new_den)

    def __sub__(self, frac2):
        if type(frac2) == float or type(frac2) == Fraction:
            new_num =  self.num * frac2.den - frac2.num * self.den
            new_den = self.den * frac2.den
        else:
            new_num = self.num - frac2 * self.den
            new_den = self.den
        return Fraction(new_num, new_den)


    def __mul__(self, frac2):
        new_num = self.num * frac2.num
        new_den = self.den * frac2.den
        return Fraction(new_num, new_den)

    def __truediv__(self, frac2):
        new_num = self.num * frac2.den
        new_den = self.den * frac2.num
        return Fraction(new_num, new_den)

    def __gt__(self, frac2):
        print('__gt__ is working')
        return (self.num/self.den) - (frac2.num/frac2.den) > 0

    def __ge__(self, frac2):
        return (self.num/self.den) - (frac2.num/frac2.den) >= 0

    def __ne__(self, frac2):
        return (self.num/self.den) != (frac2.num/frac2.den)

    def __repr__(self):
        return '<{0}.{1} object at {2}>'.format(
        type(self).__module__, type(self).__qualname__, hex(id(self)))

    



def GCD(x, y):
    while x % y != 0:
        old_x = x
        old_y = y

        x = old_y
        y = old_x % old_y
    return y

   
myFraction = Fraction(4, -6)
print("My fraction: {}".format(myFraction))
print("My numerator: {}".format(myFraction.get_num()))
print("My denominator: {}".format(myFraction.get_den()))
print()

num = 48
den = 18

print("GCD of {} and {} = {}".format(num, den, GCD(num, den)))
print()

frac1 = Fraction(2, -3)
frac2 = Fraction(1, 3)
frac3 = Fraction(2, 3)

print("{} + {} = {}\n".format(frac1, frac2, frac1 + frac2))
print("{} - {} = {}\n".format(frac1, frac2, frac1 - frac2))
print("{} > {} = ?\n{}\n".format(frac1, frac2, frac1 > frac2))
print("{} < {} = ?\n{}\n".format(frac1, frac2, frac1 < frac2))
print("{} >= {} = ?\n{}\n".format(frac1, frac2, frac1 >= frac2))
print("{} <= {} = ?\n{}\n".format(frac1, frac2, frac1 <= frac2))
print("{} <= {} = ?\n{}\n".format(frac1, frac3, frac1 <= frac3))
print("{} != {} = ?\n{}\n".format(frac1, frac3, frac1 != frac3))

myErrorTest = Fraction(3.0, 4)


# __radd__ is meant for trying to add int 2 + frac1. int doesn't
# knowing anything about how to handle our Fraction class, so
# using __radd__ 
print("{} {} {} = {}\n".format(frac1, '+', 2, frac1 + 2))
print("{} {} {} = {}\n".format(2, '+', frac1, 2 + frac1))


# __iadd__ works even if not defined, because __add__ is evoked
print(frac2)
frac2 += 1
print(frac2)


# __repr__ is very literal, it prints the object's location
print(repr(frac2))
print()

#help(int)


