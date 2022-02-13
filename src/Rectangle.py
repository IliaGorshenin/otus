from pythonProject.src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, name, a, b):
        super().__init__(name, 4)
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter_rectangle(self):
        return self.a * 2 + self.b * 2

    def add_area(self, figure):
        return self.area() + figure.area()
