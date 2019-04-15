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

#14.11.1.b
def merge4(x, y):
    result = []
    xi = 0
    yi = 0

    while xi < (len(x)):
        if x[xi] not in y:
            result.append(x[xi])
        xi += 1
    result.sort()
    return result

#14.11.1.d
def merge2(x, y):
    result = []
    xi = 0
    yi = 0

    while xi < (len(x)):
        if x[xi] not in y:
            result.append(x[xi])
        xi += 1
    result.extend(y[yi:])
    result.sort()
    return result

#print(merge2([5,7,11,11,11,12,13], [7,8,11]))


#14.11.1.e
def merge3(xs, ys):
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

#print(merge3([5,7,11,11,11,12,13], [7,8,11]))



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
        if x[i] == 0:
            i += 1
            continue
        if x[i] == 2:
            result.append(x[i])
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

#primes in a number
def primesN(x):
    result = []
    for num in range(49):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                result.append(num)
    return result

print(primesN(49))

#14.11.5.e
def prime_misses(x):
    result = []
    num = 49
    primesPresent = []
    primes = primesN(num)
    xi = 0
    i = 0
    for i in range(len(x)):
        primesPresent.append(primes_in(x[i]))
    for xi in range(len(primesPresent)):
        if xi == (len(primesPresent)-1):
            break
        else:
            result.extend(merge2(primesPresent[xi], primesPresent[xi+1]))
    result.sort()
    primesMissing = merge4(primes, result)
    return primesMissing

print(prime_misses(my_tickets))

#print(lotto_match([42,4,7,11,1,13], [2,5,7,11,13,17]))

test(lotto_match([42,4,7,11,1,13], [2,5,7,11,13,17]) == 3)
test(lotto_matches([42,4,7,11,1,13], my_tickets) == [1,2,3,1])
#test(primes_in([42, 4, 7, 11, 1, 13]) == 3)
test(prime_misses(my_tickets) == [3, 29, 47])


#14.11.5.f
def draw_average(x):
    i = 0
    xi = 0
    count = 0
    match = 0
    average = 0
    while i < 20:
        draw = lotto()
        count += 1
        for xi in range(len(x)):
            if (lotto_match(draw, x[xi])) == 5:
                match += 1
                i += 1
                average += count                
                print("We've got a 5 number match on the {0}th draw!"
                                                    .format(count))
                count = 0
                break
            #print("We've got {0} matches in the ticket with number {1}!"
            #                  .format(lotto_match(draw, x[xi]), xi+1))
    print(average/20)
draw_average(my_tickets)