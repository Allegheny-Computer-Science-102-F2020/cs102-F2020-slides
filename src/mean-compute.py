def compute_mean(numbers):
    print(f"Called compute_mean with numbers = {numbers}")
    s = sum(numbers)
    print(f"Sum of numbers = {s}")
    N = len(numbers)
    print(f"Length of numbers = {N}")
    mean = s / N
    print(f"Calculated mean = {mean}")
    return mean


numbers = [5,10,5,10,5]
print(str(compute_mean(numbers)))

numbers = [5,1,7,99,4]
print(str(compute_mean(numbers)))


from typing import List


def compute_mean_again(numbers_list: List):
    s = sum(numbers_list)
    N = len(numbers_list)
    mean = s / N
    return mean


numbers = [5,5,5,5,5]
print(str(compute_mean_again(numbers)))
