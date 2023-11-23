from math import gcd

def add_frac(frac1, frac2):        # frac1 + frac2

    if (frac1[1] == 0 or frac2[1] == 0):
        raise ValueError()
    
    result = [0, 0]

    result[1] = frac1[1] * frac2[1]
    result[0] = frac1[0] * frac2[1] + frac1[1] * frac2[0]

    gcd_ = gcd(result[0], result[1])

    result[0] //= gcd_
    result[1] //= gcd_
    
    return result

def sub_frac(frac1, frac2):        # frac1 - frac2

    if (frac1[1] == 0 or frac2[1] == 0):
        raise ValueError()
    
    result = [0, 0]

    result[1] = frac1[1] * frac2[1]
    result[0] = frac1[0] * frac2[1] - frac1[1] * frac2[0]

    gcd_ = gcd(result[0], result[1])

    result[0] //= gcd_
    result[1] //= gcd_
    
    return result

def mul_frac(frac1, frac2):        # frac1 * frac2

    if (frac1[1] == 0 or frac2[1] == 0):
        raise ValueError()
    
    result = [0, 0]

    result[0] = frac1[0] * frac2[0]
    result[1] = frac1[1] * frac2[1]

    gcd_ = gcd(result[0], result[1])

    result[0] //= gcd_
    result[1] //= gcd_
    
    return result

def div_frac(frac1, frac2):        # frac1 / frac2

    if (frac1[1] == 0 or frac2[1] == 0):
        raise ValueError()

    result = [0, 0]
    
    result[0] = frac1[0] * frac2[1]
    result[1] = frac1[1] * frac2[0]
    
    gcd_ = gcd(result[0], result[1])
    
    result[0] //= gcd_
    result[1] //= gcd_
    
    return result

def is_positive(frac):             # bool, czy dodatni

    if frac[1] == 0:
        raise ValueError()
    
    return (frac[0] > 0 and frac[1] > 0) or (frac[0] < 0 and frac[1] < 0)

def is_zero(frac):                 # bool, typu [0, x]

    if frac[1] == 0:
        raise ValueError()
    
    return frac[0] == 0

def cmp_frac(frac1, frac2):        # -1 | 0 | +1

    if (frac1[1] == 0 or frac2[1] == 0):
        raise ValueError()

    result = [0, 0]
    
    result[0] = frac1[0] * frac2[1]
    result[1] = frac1[1] * frac2[0]
    
    if result[0] < result[1]:
        return -1
    elif result[0] > result[1]:
        return 1
    else:
        return 0

def frac2float(frac):              # konwersja do float

    if frac[1] == 0:
        raise ValueError()

    return float(frac[0] / frac[1])

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([7, 8], [2, 5]), [51, 40])
        self.assertEqual(add_frac([1, 6], [2, 7]), [19, 42])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([7, 8], [2, 5]), [19, 40])
        self.assertEqual(sub_frac([1, 6], [2, 7]), [-5, 42])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([7, 8], [2, 5]), [7, 20])
        self.assertEqual(mul_frac([1, 6], [2, 7]), [1, 21])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([7, 8], [2, 5]), [35, 16])
        self.assertEqual(div_frac([1, 6], [2, 7]), [7, 12])

    def test_is_positive(self):
        self.assertEqual(is_positive([5, 6]), True)
        self.assertEqual(is_positive([-5, 6]), False)

    def test_is_zero(self):
        self.assertEqual(is_zero([0, 3]), True)
        self.assertEqual(is_zero([1, 3]), False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([5, 6], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 3], [1, 3]), 0)
        self.assertEqual(cmp_frac([1, 3], [5, 6]), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float([3, 4]), 0.75)
        self.assertEqual(frac2float([5, 2]), 2.5)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy