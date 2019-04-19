import math
from turtle import Turtle

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

    #15.12.2
    def reflect_x(self):
        my = self.y * (-1)
        return Point(self.x, my)

p = Point(3, 4)
q = Point(5, 8)

tess = Turtle()
alex = Turtle()

print(Point(3, 5).reflect_x())

print(p.x, p.y, q.x, q.y)


def midpoint(p1, p2):
    """ Return the midpoint of points p1 and p2 """
    mx = (p1.x + p2.x)/2
    my = (p1.y + p2.y)/2
    return Point(mx, my)

#print(Point(3, 4).halfway(Point(5, 12)))

#15.12.1
def distance(p1, p2):
    dx = p1.y - p1.x
    dy = p2.y - p2.x
    return math.sqrt((dx)**2 + (dy)**2)

print(distance(p, q))

