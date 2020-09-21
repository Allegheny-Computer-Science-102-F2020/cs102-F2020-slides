#!/bin/python3

import math

def sqrt(number: int, tolerance: float):
    guess = 1.0
    while abs(number - guess*guess) > tolerance:
        guess = guess - (guess*guess - number)/(2*guess)
    return guess

print()

n = 4
guess = 1.0
while abs(n - guess*guess) > 0.0001:
    guess = guess - (guess*guess - n)/(2*guess)
root = guess

print("The square root of " + str(n) + " is " + str(root))
print()

print("The square root of " + str(n) + " is " + str(math.sqrt(n)))
print()


print("The square root of " + str(n) + " is " + str(sqrt(n, 0.0001)))
print()
