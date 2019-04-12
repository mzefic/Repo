import time
from unit_tester import test
#import list_algorithms
import random

def merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            result.extend(ys[yi:]) # Add remaining items from ys
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1


#14.11.1.a
def merge1(xs, ys):
    result = []
    xi = 0
    y1 = 0

    while xi < (len(ys)):
        if xs[xi] in ys:
            result.append(xs[xi])
        xi += 1
    return result

#print(merge1([0,4,7,5,2,6,1,3],[8,1,3,9,6,4,2,5]))

#14.11.1.d
def merge2(xs, ys):
    result = []
    xi = 0
    yi = 0

    while xi < (len(xs)):
        if xs[xi] in ys[yi:]:
            del ys[yi]
            yi += 1
            xi += 1
        elif xs[xi] not in ys[yi:]:
            result.append(xs[xi])
            xi += 1
    return result

#print(merge2([5,7,11,11,11,12,13], [7,8,11]))



my_tickets = [ [ 7, 17, 37, 19, 23, 43],
               [ 7,  2, 13, 41, 31, 43],
               [ 2,  5,  7, 11, 13, 17],
               [13, 17, 37, 19, 23, 43] ]

#14.11.5.a
def lotto():
    import random
    rng = random.Random()
    draw = list(range(49))
    return rng.sample(draw, 6)

x = [42,4,7,11,1,13]
y = [42,4,7,11,1,13]
#print(lotto())


#14.11.5.b
def lotto_match(x, y):
    result = []
    xi = 0
    while xi < len(y):
        if x[xi] in y:
            result.append(x[xi])
        xi += 1
    return len(result)

#14.11.5.c
def lotto_matches(x, y):
    result = []
    i = 0
    while i < len(my_tickets):
        result.append(lotto_match(x, my_tickets[i]))
        i += 1
    return result


#14.11.5.d
def primes_in(x):
    i = 0
    g = 0
    result = []
    while i < len(x):
        if x[i] == 1:
            i += 1
            continue
        for g in range(2, x[i]):
            if (x[i] % g) == 0:
                i += 1
                break
            else:
                result.append(x[i])
                i += 1
                break
    return result


#14.11.5.e
def prime_misses(x):
    result = []
    primesPresent = []
    primes = []
    xi = 0
    i = 0
    num = 49
    for i in range(len(x)):
        primesPresent.append(primes_in(x[i]))
    for i in range(2, num):
        if (num % i) == 0:
            i += 1
        else:
            primes.append(i)
            i += 1
    while xi < len(primes):
        if primesPresent[xi] in primes:
            result.append(x[xi])
        xi += 1
    return len(result)


#print(lotto_match([42,4,7,11,1,13], [2,5,7,11,13,17]))

test(lotto_match([42,4,7,11,1,13], [2,5,7,11,13,17]) == 3)
test(lotto_matches([42,4,7,11,1,13], my_tickets) == [1,2,3,1])
test(primes_in([42, 4, 7, 11, 1, 13]) == 3)
test(prime_misses(my_tickets) == [3, 29, 47])
