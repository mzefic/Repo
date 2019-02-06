import sys
import string

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
    #test(mysum([1, 2, 3, 4]) == 10)
    #test(mysum([1.25, 2.5, 1.75]) == 5.5)
    #test(mysum([1, -2, 3]) == 2)
    #test(mysum([ ]) == 0)
    #test(mysum(range(11)) == 55)  # 11 is not included in the list.


julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")

def test_function(x):
    """  Test function to check if you can pass 'tuffle' as an argument to a function  """
    if x[2] == 1967:
        return True

#Passing 'tuffle' as an argument to a function
print(test_function(julia))

#test_suite()        # Here is the call to run the tests