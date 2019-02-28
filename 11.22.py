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
    test(dot_product([1, 1], [1, 1]) ==  2)
    test(dot_product([1, 2], [1, 4]) ==  9)
    test(dot_product([1, 2, 1], [1, 4, 3]) == 12)

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


test_suite()        # Here is the call to run the tests