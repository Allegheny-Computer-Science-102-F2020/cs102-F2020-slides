def plus(number_one, number_two):
    return number_one + number_two


def reduce(f, sequence, initial):
    result = initial
    for value in sequence:
        result = f(result, value)
    return result


numbers = [1, 2, 3, 4, 5]
added_numbers = reduce(plus, numbers, 0)
print(added_numbers)
