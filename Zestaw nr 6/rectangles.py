from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):         # "[(x1, y1), (x2, y2)]"

        string = '[' + str(self.pt1) + ', ' + str(self.pt2) + ']'

        return string

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
    
        string = 'Rectangle(' + str(self.pt1.x) + ', ' + str(self.pt1.y) + ', ' + str(self.pt2.x) + ', ' + str(self.pt2.y) + ')'

        return string

    def __eq__(self, other):   # obsługa rect1 == rect2

        return (self.pt1 == other.pt1) and (self.pt2 == other.pt2)

    def __ne__(self, other):        # obsługa rect1 != rect2

        return not self == other

    def center(self):          # zwraca środek prostokąta

        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):            # pole powierzchni

        return abs((self.pt1.x - self.pt2.x) * (self.pt1.y - self.pt2.y))

    def move(self, x, y):      # przesunięcie o (x, y)

        self.pt1 += Point(x, y)
        self.pt2 += Point(x, y)

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rect1 = Rectangle(1, 1, 8, 5)
        self.rect2 = Rectangle(-2, -6, 2, -1)
        self.rect3 = Rectangle(1, 1, 8, 5)

    def test_str(self):
        self.assertEqual(self.rect1.__str__(), "[(1, 1), (8, 5)]")
        self.assertEqual(self.rect2.__str__(), "[(-2, -6), (2, -1)]")	

    def test_repr(self):
        self.assertEqual(self.rect1.__repr__(), "Rectangle(1, 1, 8, 5)")
        self.assertEqual(self.rect2.__repr__(), "Rectangle(-2, -6, 2, -1)")

    def test_eq(self):
        self.assertEqual(self.rect1 == self.rect2, False)
        self.assertEqual(self.rect1 == self.rect3, True)

    def test_center(self):
        self.assertEqual(self.rect1.center(), Point(4.5, 3))
        self.assertEqual(self.rect2.center(), Point(0, -3.5))

    def test_area(self):
        self.assertEqual(self.rect1.area(), 28)
        self.assertEqual(self.rect2.area(), 20)

    def test_move(self):
        self.rect1.move(-1, 1)
        self.rect2.move(2, 1)
        self.assertEqual(self.rect1, Rectangle(0, 2, 7, 6))
        self.assertEqual(self.rect2, Rectangle(0, -5, 4, 0))

if __name__=='__main__':
    unittest.main()