import math
from pythonProject.src.Figure import Figure


class Circle(Figure):
    def __init__(self, name, radius_circle):
        super().__init__(name, 1)
        self.radius = radius_circle

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter_circle(self):
        return math.pi * (self.radius * 2)

    def add_area(self, figure):
        return figure.area() + self.area()
