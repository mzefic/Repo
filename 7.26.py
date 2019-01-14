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
    test(mysum([1, 2, 3, 4]) == 10)
    test(mysum([1.25, 2.5, 1.75]) == 5.5)
    test(mysum([1, -2, 3]) == 2)
    test(mysum([ ]) == 0)
    test(mysum(range(11)) == 55)  # 11 is not included in the list.


def mysum(xs):
    """ Sum all the numbers in the list xs, and return the total. """
    running_total = 0
    for x in xs:
        running_total = running_total + x
    return running_total

def seq3np1(n):
    """ Print the 3n+1 sequence from n,
        terminating when it reaches 1.
    """
    while n != 1:
        print(n, end=", ")
        if n % 2 == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    print(n, end=".\n")

def num_digits(n):
    count = 0
    while n != 0:
        count = count + 1
        n = n // 10
    return count

print(num_digits(5))

test_suite()        # Here is the call to run the tests

seq3np1(27)

for x in range(13):   # Generate numbers 0 to 12
    print(x, "\t", 2**x)

for i in range(1, 7):
    print(2 * i, end="   ")
print()

