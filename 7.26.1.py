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
    #test(mysum([1, 2, 3, 4]) == 10)
    #test(mysum([1.25, 2.5, 1.75]) == 5.5)
    #test(mysum([1, -2, 3]) == 2)
    #test(mysum([ ]) == 0)
    #test(mysum(range(11)) == 55)  # 11 is not included in the list.
    #test(count_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5)
    #test(sum_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30)
    #test(sum_words(["gggg", "ggggg", "ggggg", "ggggg", "gggg"]) == 3)
    #test(sum_words_upto(["gggg", "ggggg", "ggggg", "ggggg", "sam", "gggg", "ggg"]) == 5)


def count_odd(x):
    """ Count odd numbers in a given list """
    count = 0
    for i in x:
        if i % 2 == 1:
            count += 1
    return count

def sum_list(x):
    sumE = 0
    sumN = 0
    countO = 0
    for i in x:
        if i % 2 == 1:
            countO += 1
        if i % 2 == 0:
            sumE += i
        if i < 0:
            sumN += i
    print("The count of odd numbers is", countO)
    print("The sum of even numbers is", sumE)
    print("The sum of negative numbers is", sumN)

def sum_words(x):
    count = 0
    for i in x:
        if len(i) == 5:
            count += 1
    return count

def sum_wo_even(x):
    sum = 0
    for i in x:
        if i % 2 == 0:
            continue
        sum += i
    return sum

def first_even(x):
    num = 0
    for i in x:
        if x % 2 == 0:
            num += x
            break
    return num

def sum_wo_1even(x):
    sum = 0
    even = 0
    sum1 = 0
    for i in x:
        sum += i
    for i in x:
        if i % 2 == 0:
            even += i
            break
    sum1 = sum - even
    return sum1


def sum_words_upto(x):
    count = 0
    for i in x:
        if i == "sam":
            count += 1
            break
        count += 1
    return count

#def sqrt(n):
#    approx = n/2.0     # Start with some or other guess at the answer
#    while True:
#        better = (approx + n/approx)/2.0
#        if abs(approx - better) < 0.001:
#            return better
#        approx = better

def print_multiples(n, high):
    for i in range(1, high+1):
        print(n * i, end="   ")
    print()

def print_mult_table(high):
    for i in range(1, high+1):
        print_multiples(i, i+1)


def print_triangular_numbers(n):
    for i in range (1, n+1):
        print(i, "   ", int(i*(i+1)/2))

def is_prime(x):
    num = x
    if num > 1:
    # check for factors
        for i in range(2,num):
           if (num % i) == 0:
               print(num,"is not a prime number")
               print(i,"times",num//i,"is",num)
               break
        else:
           print(num,"is a prime number")

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        print(num,"is not a prime number")

def num_digits(n):
    count = 0
    if n == 0:
        return 1
    while n != 0:
        count = count + 1
        n = abs(n) // 10
    return count


def num_even_digits(n):
    count = 0
    if n == 0:
        return 1
    while n != 0:
        if n % 2 == 0:
            count = count + 1
        n = abs(n) // 10
    return count


def sum_of_squares(x):
    sum = 0
    sqr = 0
    for i in x:
        sqr = i ** 2
        sum += sqr
    return sum



test_suite()        # Here is the call to run the tests

#test(sum_of_squares([2, 3, 4]) == 29)
#test(sum_of_squares([ ]) == 0)
#test(sum_of_squares([2, -3, 4]) == 29)

#print(sum_of_squares([2, 3, 4]))

#test(num_even_digits(1263463456) == 6)
#test(num_even_digits(26456468) == 7)
#test(num_even_digits(7575) == 0)
#test(num_even_digits(0) == 1)

#test(num_digits(0) == 1)
#test(num_digits(-12345) == 5)

#print(sum_wo_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -5]))
#print(sum_wo_1even([4, 1, 3, 4, 5, 6, 7]))
#print(sum_words_upto(["gggg", "sam", "ggggg", "ggggg", "ggg", "ggg", "ggg"]))
#print(sqrt(25.0))
#print_mult_table(7)
#print_triangular_numbers(5)
