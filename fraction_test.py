import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())

    # TODO Write tests for __init__, __eq__, +, *.
    # Here is an example, but you must add more test cases.  
    # The test requires that your __eq__ is correct.
    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3,4), Fraction(1,12)+Fraction(2,3))
        # 2/3 = 1/6 + 1/2
        self.assertEqual(Fraction(2,3), Fraction(1,6)+Fraction(1,2))
        # 1/4 = 1/20 + 1/5
        self.assertEqual(Fraction(1,4), Fraction(1,20)+Fraction(1,5))

    def test_sub(self):
        # 7/12 = 2/3 - 1/12
        self.assertEqual(Fraction(7,12), Fraction(2,3)-Fraction(1,12))
        # 1/3 = 1/2 - 1/6
        self.assertEqual(Fraction(1,3), Fraction(1,2)-Fraction(1,6))
        # 3/10 = 5/10 - 4/20
        self.assertEqual(Fraction(3,10), Fraction(5,10)-Fraction(4,20))

    def test_mul(self):
        self.assertEqual(Fraction(1,30), Fraction(1,5) * Fraction(1,6))
        self.assertEqual(Fraction(2,15), Fraction(2,3) * Fraction(1,5))
        self.assertEqual(Fraction(10,13), Fraction(-1)  *  Fraction(-10,13,))
       

    def test_eq(self):
        f = Fraction(1,2)
        g = Fraction(-40,-80)     
        h = Fraction(10000,20001) # not quite 1/2
        k = Fraction(0)
        j = Fraction(1,0)
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        self.assertFalse(k.__eq__(f))
        self.assertFalse(j.__eq__(k))

    def test_gt(self):
        w = Fraction(2,3)
        e = Fraction(1,3)
        self.assertTrue(w > e)
        self.assertTrue(w.__gt__(e))
        q = Fraction(4,5)
        r = Fraction(6,7)
        self.assertFalse(q > r)
        self.assertFalse(q.__gt__(r))
        o = Fraction(7,19)
        u = Fraction(21,31)
        self.assertFalse(o > u)
        self.assertFalse(o.__gt__(u))

        
