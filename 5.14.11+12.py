a = 5
b = 4
c = 6

def find_hypot(x, y):
    c = (x**2 + b**2)**0.5
    return c

def is_rightangled(x, y, z):
    if x>y and x>z:                                  # Find the hypothenuse and asign the sides
        hypo = x; y = a; z = b
    if z>x and z>y:
        hypo = z; x = a; y = b
    if y>x and y>z:
        hypo = y; x = a; z = b
    if abs(hypo - ((a**2 + b**2)**0.5)) < 0.9:       # Round up floating numbers and check if the equation is true
        print("True")
    else:
        print("False")

print (find_hypot(a, b))
print (is_rightangled(a, b, c))