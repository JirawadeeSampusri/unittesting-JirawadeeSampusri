import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(2, 0)
        self.assertEqual("1/0", f.__str__())
        f = Fraction(6, 9)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-60, 20)
        self.assertEqual("-3", f.__str__())
        f = Fraction(36, -48)
        self.assertEqual("-3/4", f.__str__())
        # Constructor should provide default denominato
        # r = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())
        f = Fraction(0, 0)
        self.assertEqual("0/0", f.__str__())

    def test_init(self):
        f = Fraction(3)
        self.assertEqual(3, f.numerator)
        f = Fraction(3)
        self.assertEqual(1, f.denominator)
        f = Fraction(-2, 3)
        self.assertEqual(-2, f.numerator)
        f = Fraction(1, -2)
        self.assertEqual(2, f.denominator)
        f = Fraction(-5, -6)
        self.assertEqual(5, f.numerator)
        f = Fraction(0, 0)
        self.assertEqual(0, f.numerator)

    # TODO Write tests for __init__, __eq__, +, *.
    # Here is an example, but you must add more test cases.  
    # The test requires that your __eq__ is correct.
    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3,4), Fraction(1,12)+Fraction(2,3))
        # -1/3 = 1/6 + 1/2
        self.assertEqual(Fraction(-1,3), Fraction(1,6)+Fraction(-1,2))
        # 1 = 1/2 + -20/-40
        self.assertEqual(Fraction(1), Fraction(1, 2) + Fraction(-20, -40))
        # 0/0 = 3/0 + 3/0
        self.assertTrue(math.isnan(Fraction(3,0) + Fraction(3,0)))
        # nan = 0/0 + 2/3
        self.assertTrue(math.isnan(Fraction(0, 0) + Fraction(2, 3)))

    def test_sub(self):
        # 7/12 = 2/3 - 1/12
        self.assertEqual(Fraction(7,12), Fraction(2,3)-Fraction(1,12))
        # 1/6 = 1/3 - 1/6
        self.assertEqual(Fraction(1,6), Fraction(1,3)-Fraction(1,6))
        # 1/10 = 9/10 - 4/5
        self.assertEqual(Fraction(1,10), Fraction(9,10)-Fraction(4,5))
        # 0/0 = 3/0 - 2/0
        self.assertTrue(math.isnan(Fraction(0,0), Fraction(3,0)-Fraction(2,0)))
        # 0/0 = 5/0 - 0/2
        self.assertTrue(math.isnan(Fraction(0,0), Fraction(5,0)-Fraction(0,2)))

    def test_mul(self):
        # 1/30 = 1/5 * 1/6
        self.assertEqual(Fraction(1,30), Fraction(1,5) * Fraction(1,6))
        # 1/21 = 2/7 * 1/6
        self.assertEqual(Fraction(1,21), Fraction(2,7) * Fraction(1,6))
        # -1/12 = 1/2 * 1/6
        self.assertEqual(Fraction(-1,12), Fraction(-1,2) * Fraction(1,6))
        # 1/3 = 2/3 * 2/4
        self.assertEqual(Fraction(1,3), Fraction(2,3) * Fraction(2,4))
        # nan = 2/4 * -1/0
        self.assertTrue(math.isnan(Fraction(2, 4) * Fraction(-1, 0)))

 

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

if __name__ == '__main__':
    unittest.main(verbosity=2)    
