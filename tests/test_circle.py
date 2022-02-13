from pythonProject.src.Circle import Circle
import math
from pythonProject.src.Triangle import Triangle


name = 'Круг'
a = 3


def test_create_class():
    circle = Circle(name, a)
    assert circle.sides() == 1
    assert isinstance(circle, Circle)


def test_area():
    circle = Circle(name, a)
    assert circle.area() == math.pi * 3 ** 2


def test_perimeter():
    circle = Circle(name, a)
    assert circle.perimeter_circle() == math.pi * 3 * 2


def test_add_area():
    b = 5
    c = 7
    triangle = Triangle(name, a, b, c)
    triangle.area()
    circle = Circle(name, a)
    circle.area()
    assert (circle.add_area(triangle)) == triangle.area() + circle.area()
