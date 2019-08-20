import math
class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        self.numerator = numerator
        self.denominator = denominator

    #TODO Write the __add__ method, and remove this TODO comment.
    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        numerator =   (self.numerator * frac.denominator)+(self.denominator*frac.numerator)
        denominator =   self.denominator * frac.denominator
        gcd_num = math.gcd(numerator,denominator)
        numerator/= gcd_num
        denominator /= gcd_num
        return Fraction(numerator, denominator)


    def __mul__(self,frac):
        numerator = self.numerator*frac.numerator
        denominator = self.denominator*frac.denominator
        gcd_num = math.gcd(numerator,denominator)
        numerator/= gcd_num
        denominator /= gcd_num 
        return Fraction(numerator, denominator)



    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        gcd_num1 = math.gcd(self.numerator,self.denominator)
        self.numerator/= gcd_num1
        self.denominator /= gcd_num1
        gcd_num2 = math.gcd(self.numerator,self.denominator)
        frac.numerator/= gcd_num2
        frac.denominator /= gcd_num2
        return self.numerator == frac.numerator and self.denominator == frac.denominator

    def __repr__(self):
        return"{}/{}".format(int(self.numerator),int(self.denominator))
