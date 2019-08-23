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
        if denominator < 0:
            if numerator > 0:
                numerator = numerator * (-1)
            else:
                numerator = abs(numerator)
            denominator = abs(denominator)

        elif denominator == 0:
            if numerator < 0:
                numerator = -1
            elif numerator >= 0:
                numerator = 1

        gcd = math.gcd(numerator, denominator)
        self.numerator = int(numerator/gcd)
        self.denominator = int(denominator/gcd)

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        numerator = (self.numerator * frac.denominator) + (self.denominator * frac.numerator)
        denominator = self.denominator * frac.denominator

        if frac.denominator == 0 and self.denominator == 0:
            if frac.numerator > 0 and self.numerator > 0:
                return Fraction(numerator=1, denominator=0)
            elif frac.numerator < 0 and self.numerator < 0:
                return Fraction(numerator=-1, denominator=0)
            else:
                return Fraction(numerator=0, denominator=0)

        elif frac.denominator != 0 and self.denominator != 0:
            return Fraction(numerator, denominator)

        elif self.denominator == 0 and frac.denominator != 0:
            if self.numerator > 0 and frac.numerator != 0:
                return Fraction(numerator=1, denominator=0)
            elif self.numerator < 0 and frac.numerator != 0:
                return Fraction(numerator=-1, denominator=0)
            elif self.numerator == 0 and frac.numerator != 0:
                return Fraction(numerator=0, denominator=0)

        elif self.denominator != 0 and frac.denominator == 0:
            if self.numerator > 0 and frac.numerator != 0:
                return Fraction(numerator=1, denominator=0)
            elif self.numerator < 0 and frac.numerator != 0:
                return Fraction(numerator=-1, denominator=0)
            elif self.numerator == 0 and frac.numerator != 0:
                return Fraction(numerator=0, denominator=0)

    def __mul__(self, frac):
        numerator = self.numerator * frac.numerator
        denominator = self.denominator * frac.denominator

        if self.denominator == 0 and frac.denominator == 0:
            if frac.numerator == 0:
                return Fraction(numerator=0, denominator=0)
            elif (self.numerator > 0 and frac.numerator > 0) or (self.numerator < 0 and frac.numerator < 0):
                return Fraction(numerator=1, denominator=0)
            elif (self.numerator < 0 and frac.numerator > 0) or (self.numerator > 0 and frac.numerator < 0):
                return Fraction(numerator=-1, denominator=0)

        elif frac.denominator != 0 and self.denominator != 0:
            return Fraction(numerator, denominator)

        elif self.denominator == 0 and frac.denominator != 0:
            if frac.numerator != 0 and self.numerator > 0:
                return Fraction(numerator=1, denominator=0)
            elif frac.numerator != 0 and self.numerator < 0:
                return Fraction(numerator=-1, denominator=0)
            elif self.numerator == 0 and frac.numerator != 0:
                return Fraction(numerator=0, denominator=0)

        elif self.denominator != 0 and frac.denominator == 0:
            return Fraction(numerator=0, denominator=0)

    def __str__(self):
        if self.denominator == 1:
            return f"{self.numerator}"
        else:
            return f"{self.numerator}/{self.denominator}"

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        return self.numerator == frac.numerator and self.denominator == frac.denominator
