#!/bin/python3

import math

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
