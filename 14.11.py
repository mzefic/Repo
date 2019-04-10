import time
from unit_tester import test
import list_algorithms

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
            yi += 1
        elif xs[xi] not in ys:
            result.append(xs[xi])
            xi += 1
    return result

print(merge2([5,7,11,11,11,12,13], [7,8,11]))