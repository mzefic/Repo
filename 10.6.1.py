import turtle

turtle.setup(400,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen")             # Set the background color
tess = turtle.Turtle()               # Create our favorite turtle
x = 3

# The next four functions are our "event handlers".
def pen(x):
    tess.pensize(x)

def h1():
   tess.forward(30)

def h2():
   tess.left(45)

def h3():
   tess.right(45)

def h4():
    wn.bye()                        # Close down the turtle window

def h5():
   tess.color("red")

def h6():
   tess.color("green")

def h7():
   tess.color("blue")

def h8():
    global x
    if x>=20:
        pen(20)
    else:
        x += 1
        pen(x)

def h9():
    global x
    if x<=1:
        pen(1)
    else:
        x -= 1
        pen(x)

# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(h5, "R")
wn.onkey(h6, "G")
wn.onkey(h7, "B")
wn.onkey(h8, "+")
wn.onkey(h9, "-")


# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()