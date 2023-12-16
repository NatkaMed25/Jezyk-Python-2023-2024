from points import Point
from rectangles import Rectangle
    
def test_from_points():
    rectangle = Rectangle.from_points((Point(1, 1), Point(8, 5)))
    assert str(rectangle) == '[(1, 1), (8, 5)]'


def test_properties():
    rectangle = Rectangle(1, 1, 8, 5)

    assert rectangle.top == 5
    assert rectangle.bottom == 1
    assert rectangle.left == 1
    assert rectangle.right == 8
    assert rectangle.width == 7
    assert rectangle.height == 4
    assert rectangle.topleft == Point(1, 5)
    assert rectangle.topright == Point(8, 5)
    assert rectangle.bottomleft == Point(1, 1)
    assert rectangle.bottomright == Point(8, 1)
    assert rectangle.center == Point(4.5, 3)
