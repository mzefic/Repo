a = 5
b = 4
c = 3

def find_hypot(x, y):
    c = (x**2 + b**2)**0.5
    return c

def is_rightangled(x, y, z):
    if x>y and x>z:
        hypo = x; y = a; z = b
    if z>x and z>y:
        hypo = z; x = a; y = b
    if y>x and y>z:
        hypo = y; x = a; z = b
    if hypo == int((a**2 + b**2)**0.5):
        print("True")
    else:
        print("False")

print (find_hypot(a, b))
print (is_rightangled(a, b, c))