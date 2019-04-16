from turtle import Turtle

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

p = Point()
q = Point()

tess = Turtle()
alex = Turtle()

print(p.x, p.y, q.x, q.y)
