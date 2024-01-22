from abc import ABC


class Shape(ABC):
    def __str__(self):
        return ''


class Circle(Shape):
    def __init__(self, radius=0.0):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f'A circle of radius {self.radius}'


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'A square with side {self.side}'


class ColoredShape(Shape):
    def __init__(self, shape, color):
        if isinstance(shape, ColoredShape):
            raise Exception('Cannot apply ColoredDecorator twice')
        self.shape = shape
        self.color = color

    def __str__(self):
        return f'{self.shape} has the color {self.color}'


circle = Circle(2)
print(circle)

red_circle = ColoredShape(circle, "red")
print(red_circle)

