#!/bin/python3

def factorial(number: int):
    if number == 1:
        return 1
    return number * factorial(number - 1)

num = 5
print()
print("The factorial of " + str(num) + " is " + str(factorial(num)))
print()
