import math

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):         # zwraca string "(x, y)"

        string = '(' + str(self.x) + ', ' + str(self.y) + ')'

        return string

    def __repr__(self):        # zwraca string "Point(x, y)"

        string = 'Point(' + str(self.x) + ', ' + str(self.y) + ')'

        return string

    def __eq__(self, other):   # obsługa point1 == point2

        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):        # obsługa point1 != point2

        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2

        x_add = self.x + other.x
        y_add = self.y + other.y

        return Point(x_add, y_add)

    def __sub__(self, other):  # v1 - v2

        x_sub = self.x - other.x
        y_sub = self.y - other.y

        return Point(x_sub, y_sub)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę

        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę

        return self.x * other.y - self.y * other.x

    def length(self):          # długość wektora

        return math.sqrt(self.x**2 + self.y**2)

    def __hash__(self):

        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(1, 4)	
        self.p2 = Point(2, 7)
        self.p3 = Point(-1, 5)	
        self.p4 = Point(1, 4)

    def test_str(self):
        self.assertEqual(self.p1.__str__(), "(1, 4)")
        self.assertEqual(self.p2.__str__(), "(2, 7)")

    def test_repr(self):
        self.assertEqual(self.p1.__repr__(), "Point(1, 4)")
        self.assertEqual(self.p2.__repr__(), "Point(2, 7)")

    def test_eq(self):
        self.assertEqual(self.p1 == self.p2, False)
        self.assertEqual(self.p1 == self.p4, True)

    def test_ne(self):
        self.assertEqual(self.p1 != self.p2, True)
        self.assertEqual(self.p1 != self.p4, False)

    def test_add(self):
        self.assertEqual(self.p1 + self.p2, Point(3, 11))
        self.assertEqual(self.p2 + self.p3, Point(1, 12))
    
    def test_sub(self):
        self.assertEqual(self.p1 - self.p2, Point(-1, -3))
        self.assertEqual(self.p2 - self.p3, Point(3, 2))

    def test_mul(self):
        self.assertEqual(self.p1 * self.p2, 30)
        self.assertEqual(self.p2 * self.p3, 33)

    def test_cross(self):
        self.assertEqual(Point.cross(self.p1, self.p2), -1)
        self.assertEqual(Point.cross(self.p2, self.p3), 17)

    def test_length(self):
        self.assertEqual(self.p1.length(), math.sqrt(17))
        self.assertEqual(self.p2.length(), math.sqrt(53))
              
if __name__=='__main__':
    unittest.main()