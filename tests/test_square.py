from pythonProject.src.Circle import Circle
from pythonProject.src.Square import Square

name = 'Квадрат'
a = 4


def test_create_class():
    square = Square(name, a)
    assert square.sides() == 4
    assert isinstance(square, Square)


def test_area():
    square = Square(name, a)
    assert square.area() == 16


def test_perimeter():
    square = Square(name, a)
    assert square.perimeter_square() == 16


def test_add_area():
    circle = Circle(name, a)
    circle.area()
    square = Square(name, a)
    square.area()
    assert (square.add_area(circle)) == circle.area() + square.area()
