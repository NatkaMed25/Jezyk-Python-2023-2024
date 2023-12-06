from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
    # Chcemy, aby x1 < x2, y1 < y2.

        if x1 >= x2 or y1 >= y2:
            raise ValueError("x1 > x2 lub y1 > y2")

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

    def center(self):         # zwraca środek prostokąta

        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):           # pole powierzchni

        return abs((self.pt1.x - self.pt2.x) * (self.pt1.y - self.pt2.y))

    def move(self, x, y):    # przesunięcie o (x, y)

        self.pt1 += Point(x, y)
        self.pt2 += Point(x, y)

    def intersection(self, other):  # część wspólna prostokątów

        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)
        
        if (x1 > x2 or y1 > y2):
            raise ValueError("Prostokąty nie mają części wspólnej")
        return Rectangle(x1, y1, x2, y2)

    def cover(self, other):  # prostąkąt nakrywający oba

        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)

        return Rectangle(x1, y1, x2, y2)

    def make4(self):         # zwraca krotkę czterech mniejszych

        centerX = (self.pt1.x + self.pt2.x) / 2
        centerY = (self.pt1.y + self.pt2.y) / 2

        return (Rectangle(self.pt1.x, self.pt1.y, centerX, centerY),
                Rectangle(centerX, self.pt1.y, self.pt2.x, centerY),
			    Rectangle(self.pt1.x, centerY, centerX, self.pt2.y),
			    Rectangle(centerX, centerY, self.pt2.x, self.pt2.y))

# A-------B   po podziale  A---+---B
# |       |                |   |   |
# |       |                +---+---+
# |       |                |   |   |
# D-------C                D---+---C

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rect1 = Rectangle(1, 1, 8, 5)
        self.rect2 = Rectangle(-2, -6, 2, -1)
        self.rect3 = Rectangle(1, 1, 8, 5)
        self.rect4 = Rectangle(0, -2, 5, 7)

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

    def test_intersection(self):
        with self.assertRaises(ValueError) as context:
            self.assertEqual(self.rect1.intersection(self.rect2))
        self.assertEqual(self.rect3.intersection(self.rect4), Rectangle(1, 1, 5, 5))

    def test_cover(self):
        self.assertEqual(self.rect1.cover(self.rect2), Rectangle(-2, -6, 8, 5))
        self.assertEqual(self.rect3.cover(self.rect4), Rectangle(0, -2, 8, 7))

    def test_make4(self):
        self.assertEqual(self.rect1.make4(), (Rectangle(1, 1, 4.5, 3), 
			Rectangle(4.5, 1, 8, 3), Rectangle(1, 3, 4.5, 5), 
			Rectangle(4.5, 3, 8, 5)))

if __name__ == '__main__':
	unittest.main()