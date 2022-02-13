from pythonProject.src.Rectangle import Rectangle
from pythonProject.src.Square import Square

name = 'Прямоугольник'
a = 3
b = 5


def test_create_class():
    rectangle = Rectangle(name, a, b)
    assert rectangle.sides() == 4
    assert isinstance(rectangle, Rectangle)


def test_area():
    rectangle = Rectangle(name, a, b)
    assert rectangle.area() == 15


def test_perimeter():
    rectangle = Rectangle(name, a, b)
    assert rectangle.perimeter_rectangle() == 16


def test_add_area():
    square = Square(name, a)
    square.area()
    rectangle = Rectangle(name, a, b)
    rectangle.area()
    assert (rectangle.add_area(square)) == square.area() + rectangle.area()
