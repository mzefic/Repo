import turtle           # Tess becomes a traffic light.

turtle.setup(400,600)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
alex = turtle.Turtle()
gina = turtle.Turtle()
mira = turtle.Turtle()


def draw_housing1():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()
    tess.penup()

def draw_housing2():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.penup()
    tess.left(180)
    tess.forward(10)
    tess.pendown()
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.right(90)
    tess.forward(200)
    tess.circle(-40, 180)
    tess.forward(200)
    tess.left(90)
    tess.penup()
    tess.forward(10)
    tess.end_fill()
    tess.penup()


draw_housing1()
draw_housing2()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

alex.penup()
alex.back(50)
alex.left(90)
alex.forward(50)
alex.shape("circle")
alex.shapesize(3)
alex.fillcolor("green")




# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        gina.penup()
        gina.back(50)
        gina.left(90)
        gina.forward(190)
        gina.shape("circle")
        gina.shapesize(3)
        gina.fillcolor("red")
        state_num = 1
    elif state_num == 1:     # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        mira.penup()
        mira.back(50)
        mira.left(90)
        mira.forward(120)
        mira.shape("circle")
        mira.shapesize(3)
        mira.fillcolor("orange")
        state_num = 2
    else:                    # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0
    wn.ontimer(advance_state_machine, 5000)

# Bind the event handler to the space key.
#wn.onkey(advance_state_machine, "space")

wn.ontimer(advance_state_machine, 5000)
#wn.listen()                      # Listen for events
wn.mainloop()