def square(value):
    return value * value


def map(f, sequence):
    result = (  )
    for element in sequence:
        result += ( f(element), )
    return result


squared = map(square, (2, 3, 5, 7, 11))
print(squared)


squared_range = map(square, range(10))
print(squared_range)
