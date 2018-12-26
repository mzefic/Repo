import turtle

def draw_square(t):
    """Make turtle t draw a square"""
    for i in range(4):
        t.forward(20)
        t.left(90)
    t.penup()
    t.forward(40)
    t.pendown()

wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("HotPink")
alex.pensize(3)

for i in range(5):
    draw_square(alex)

wn.mainloop()

