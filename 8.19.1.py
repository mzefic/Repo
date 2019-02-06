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


fruit = "banana"
list(enumerate(fruit))
#print(len(fruit[1]))
m = fruit[0]
#print(m)

ix = 0
while ix < len(fruit):
    letter = fruit[ix]
    print(letter)
    ix += 1

def book_strings():
    prefixes = "JKLMNOPQ"
    suffix = "ack"
    for p in prefixes:
        if p == "O" or p == "Q":
            print(p + "u" + suffix)
        else:
            print(p + suffix)

#book_strings()

def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

#test(remove_punctuation('"Well, I never did!", said Alice.') == "Well I never did said Alice")
#test(remove_punctuation("Are you very, very, sure?") == "Are you very very sure")

s1 = "His name is {0}!".format("Arthur")
print(s1)


#test_suite()        # Here is the call to run the tests