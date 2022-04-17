from pythonProject.src.Figure import Figure


class Square(Figure):
    def __init__(self, name, a):
        super().__init__(name, 4)
        self.a = a

    def area(self):
        return self.a ** 2

    def perimeter_square(self):
        return self.a * 4

    def add_area(self, figure):
        return self.area() + figure.area()
