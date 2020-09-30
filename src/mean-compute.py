def compute_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s / N
    return mean


numbers = [5,10,5,10,5]
print(str(compute_mean(numbers)))


from typing import List


def compute_mean(numbers: List):
    s = sum(numbers)
    N = len(numbers)
    mean = s / N
    return mean


numbers = [5,5,5,5,5]
print(str(compute_mean(numbers)))
