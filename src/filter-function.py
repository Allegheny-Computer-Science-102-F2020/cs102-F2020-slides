def is_even(value):
    if value % 2 == 0:
        return True
    return False


def is_odd(value):
    if value % 2 == 1:
        return True
    return False


filtered_even = filter(is_even, (2, 3, 5, 7, 11))
print(list(filtered_even))


filtered_odd = filter(is_odd, (2, 3, 5, 7, 11))
print(list(filtered_odd))
