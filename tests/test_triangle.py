from pythonProject.src.Rectangle import Rectangle
from pythonProject.src.Triangle import Triangle

name = 'Треугольник'
a = 5
b = 7
c = 9


def test_create_class():
    triangle = Triangle(name, a, b, c)
    assert triangle.sides() == 3
    assert isinstance(triangle, Triangle)


def test_area():
    triangle = Triangle(name, a, b, c)
    assert triangle.area() == 17.41228014936585


def test_perimeter():
    triangle = Triangle(name, a, b, c)
    assert triangle.perimeter_triangle() == 21


def test_add_area():
    rectangle = Rectangle(name, a, b)
    rectangle.area()
    triangle = Triangle(name, a, b, c)
    triangle.area()
    assert (triangle.add_area(rectangle)) == rectangle.area() + triangle.area()
