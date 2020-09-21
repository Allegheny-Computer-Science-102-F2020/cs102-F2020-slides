#!/bin/python3

def compute_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s / N
    return mean


numbers = [5,1,7,99,4]
print(str(compute_mean(numbers)))


from typing import List


def compute_mean(numbers: List):
    s = sum(numbers)
    N = len(numbers)
    mean = s / N
    return mean


numbers = [5,1,7,99,4]
print(str(compute_mean(numbers)))
