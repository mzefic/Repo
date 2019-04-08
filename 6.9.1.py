import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    #test(absolute_value(17) == 17)
    #test(absolute_value(-17) == 17)
    #test(absolute_value(0) == 0)
    #test(absolute_value(3.14) == 3.14)
    #test(absolute_value(-3.14) == 3.14)
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)
    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)
    test(to_secs(2.5, 0, 10.71) == 9010)
    test(to_secs(2.433,0,0) == 8758)
    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)
    test(compare(5, 4) == 1)
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)
    test(hypotenuse(3, 4) == 5.0)
    test(hypotenuse(12, 5) == 13.0)
    test(hypotenuse(24, 7) == 25.0)
    test(hypotenuse(9, 12) == 15.0)
    test(slope(5, 3, 4, 2) == 1.0)
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)
    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(4, 6, 12, 8) == 5.0)
    test(is_even(5) == "False")
    test(is_even(8) == "True")
    test(is_even(18) == "True")
    test(is_even(255) == "False")
    test(is_odd(5) == "True")
    test(is_odd(8) == "False")
    test(is_odd(18) == "False")
    test(is_odd(255) == "True")

def turn_clockwise(x):
    if x == 'N':
        return "E"
    if x == 'E':
        return "S"
    if x == 'S':
        return "W"
    if x == 'W':
        return "N"


def day_name(a):
    if a==1:
        return "Monday"
    if a==2:
        return "Tuesday"
    if a==3:
        return "Wednesday"
    if a==4:
        return "Thursday"
    if a==5:
        return "Friday"
    if a==6:
        return "Saturday"
    if a==0:
        return "Sunday"
    else:
        return


def day_add(a, b):
    weekday = 0
    if a=="Monday":
        if b>0:
            weekday = (b % 7) + 1
        if b<0:
            weekday = (b % 7) - 1
    elif a=="Tuesday":
        if b>0:
            weekday = (b % 7) + 2
        if b<0:
            weekday = (b % 7) - 2
    elif a=="Wednesday":
        if b>0:
            weekday = (b % 7) + 3
        if b<0:
            weekday = (b % 7) - 3
    elif a=="Thursday":
        if b>0:
            weekday = (b % 7) + 4
        if b<0:
            weekday = (b % 7) - 4
    elif a=="Friday":
        if b>0:
            weekday = (b % 7) + 5
        if b<0:
            weekday = (b % 7) - 5
    elif a=="Saturday":
        if b>0:
            weekday = (b % 7) + 6
        if b<0:
            weekday = (b % 7) - 6
    elif a=="Sunday":
        if b>0:
            weekday = (b % 7) + 0
        if b<0:
            weekday = (b % 7) - 0
    if weekday==1:
        return "Monday"
    if weekday==2:
        return "Tuesday"
    if weekday==3:
        return "Wednesday"
    if weekday==4:
        return "Thursday"
    if weekday==5:
        return "Friday"
    if weekday==6:
        return "Saturday"
    if weekday==0:
        return "Sunday"
    else:
        return


def days_in_month(a):
    if a=="January":
        return "31"
    elif a=="February":
        d = 28
        return d
    elif a=="March":
        d = 31
        return d
    elif a=="April":
        d = 30
        return d
    elif a=="May":
        d = 31
        return d
    elif a=="June":
        d = 30
        return d
    elif a=="July":
        d = 31
        return d
    elif a=="August":
        d = 31
        return d
    elif a=="September":
        d = 30
        return d
    elif a=="October":
        d = 31
        return d
    elif a=="November":
        d = 30
        return d
    elif a=="December":
        d = 31
        return d

def to_secs(x, y, z):
    hours = x * 3600
    minutes = y * 60
    seconds = hours + minutes + z
    return int(seconds)

def hours_in(x):
    hours = x // 3600
    return hours

def minutes_in(x):
    minutes = (x % 3600) // 60
    return minutes

def seconds_in(x):
    seconds = (x % 3600) % 60
    return seconds

def compare(a, b):
    if a > b:
        return 1
    if a == b:
        return 0
    if a < b:
        return -1

def hypotenuse(a, b):
    c = ((a**2)+(b**2))**0.5
    return c

def slope(x1, y1, x2, y2):
    line_slope = (y2 - y1) / (x2 - x1)
    return line_slope

def intercept(x1, y1, x2, y2):
    line_slope = slope(x1, y1, x2, y2)
    y_intercept = y2 - (line_slope * x2)
    return float(y_intercept)

def is_even(n):
    if n % 2 == 0:
        return "True"
    else:
        return "False"

def is_odd(n):
    if n % 2 != 0:
        return "True"
    if is_even(n) == "False":
        return "True"
    else:
        return "False"

def is_factor(x, y):
    if y % x == 0:
        return True
    else:
        return False

def is_multiple(x, y):
    if is_factor(y, x) == True:
        return True
    elif is_factor(y, x) == False:
        return False
  
def f2c(t):
    celsius = (t - 32) * (5 / 9)
    return round(celsius)

def c2f(t):
    fahrenheit = (t * (9 / 5)) + 32
    return round(fahrenheit)

test_suite()        # Here is the call to run the tests

test(f2c(212) == 100)     # Boiling point of water
test(f2c(32) == 0)        # Freezing point of water
test(f2c(-40) == -40)     # Wow, what an interesting case!
test(f2c(36) == 2)
test(f2c(37) == 3)
test(f2c(38) == 3)
test(f2c(39) == 4)
test(c2f(0) == 32)
test(c2f(100) == 212)
test(c2f(-40) == -40)
test(c2f(12) == 54)
test(c2f(18) == 64)
test(c2f(-48) == -54)
