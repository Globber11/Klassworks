from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def solve_area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def solve_area(self):
        return self.r * 2 * pi

class Square(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def solve_area(self):
        return self.a * self.b

class Triangle(Shape):
    def __init__(self, a, h):
        self.a = a
        self.h = h

    def solve_area(self):
        return self.a * self.h

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, arg1=None, arg2=None):
        if shape_type == "circle":
            return Circle(arg1)
        elif shape_type == "square":
            return Square(arg1, arg2)
        elif shape_type == "triangle":
            return Triangle(arg1, arg2)
        else:
            raise ValueError("Неизвестный тип фигуры")

if __name__ == "__main__":
    shape1 = ShapeFactory().create_shape('circle', 5)
    shape2 = ShapeFactory().create_shape('square', 5, 5)
    shape3 = ShapeFactory().create_shape('triangle', 5, 5)

    print(shape1.solve_area())
    print(shape2.solve_area())
    print(shape3.solve_area())
