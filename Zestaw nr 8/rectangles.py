from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
    # Chcemy, aby x1 < x2, y1 < y2.

        if x1 >= x2 or y1 >= y2:
            raise ValueError("x1 >= x2 lub y1 >= y2")

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

    @classmethod
    def from_points(cls, points):
        pt1, pt2 = points
        return cls(pt1.x, pt1.y, pt2.x, pt2.y)
    
    @property
    def top(self):
        return self.pt2.y

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def left(self):
        return self.pt1.x

    @property
    def right(self):
        return self.pt2.x
	
    @property
    def width(self):
        return self.pt2.x - self.pt1.x

    @property
    def height(self):
        return self.pt2.y - self.pt1.y
    
    @property
    def topleft(self):
        return Point(self.pt1.x, self.pt2.y)

    @property
    def bottomleft(self):
        return Point(self.pt1.x, self.pt1.y)

    @property
    def topright(self):
        return Point(self.pt2.x, self.pt2.y)

    @property
    def bottomright(self):
        return Point(self.pt2.x, self.pt1.y)

    @property
    def center(self):
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)