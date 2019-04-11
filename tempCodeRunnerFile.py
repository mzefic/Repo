x = [42,4,7,11,1,13]
y = [42,4,7,11,1,13]
#print(lotto())


#14.11.5.b
def lotto_match(x, y):
    result = []
    xi = 0
    for xi in y:
        if x[xi] in y:
            result.append(x[xi])
        xi += 1
    return result

print(lotto_match([42,4,7,11,1,13], [2,5,7,11,13,17]))