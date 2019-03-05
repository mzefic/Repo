import sys
import math

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
    test(replace("Mississippi", "i", "I") == "MIssIssIppI")

    s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
    test(replace(s, "om", "am") == "I love spam! Spam is my favorite food. Spam, spam, yum!")

    test(replace(s, "o", "a") ==
    "I lave spam! Spam is my favarite faad. Spam, spam, yum!")

def add_vectors(u, v):
    result = []
    for i in range(len(u)):
        x = (u[i] + v[i])
        result.append(x)
    return result

def scalar_mult(s, v):
    result = []
    for i in range(len(v)):
        x = (s * v[i])
        result.append(x)
    return result

def dot_product(u, v):
    result = 0
    for i in range(len(u)):
        result += (u[i] * v[i])
    return result

def replace(s, old, new):
    result = str
    p = len(s)
    g = len(old)
    x = []
    for i in s:
        if i == old:
            i = new
        x.append(i)
    result = "".join(x)
    return result

def replace(s, old, new):
    result = "new".join(s.split("old"))
    return result


print(replace("I love spom! Spom is my favorite food. Spom, spom, yum!", "om", "am"))

test_suite()        # Here is the call to run the tests

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"

for i in range(0, len(s) -1, 2):
    print(s.find('om'))

print(s.replace('om', 'am'))

