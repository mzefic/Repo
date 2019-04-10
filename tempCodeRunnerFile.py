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