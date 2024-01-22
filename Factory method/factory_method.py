from math import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x:5.2f}, y: {self.y:5.2f}'

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * sin(theta), rho * cos(theta))


p1 = Point(2, 3)
p2 = Point.new_polar_point(1, 2)
p3 = Point.new_cartesian_point(5, 6)
p4 = Point.new_polar_point(7, 8)
print(p1, p2, p3, p4, sep='\n')
