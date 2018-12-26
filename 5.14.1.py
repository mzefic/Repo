x=-1

def print_square_root(x):
    if x <= 0:
        print("Positive numbers only, please.")


    result = x**0.5
    print("The square root of", x, "is", result)
    return result

print_square_root(x)