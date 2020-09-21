#!/bin/python3

def square(number: int):
    return number * number


def call_twice(f, number: int):
    return f(f(number))


number = 5
result = call_twice(square, number)

print()
print("Calling the square twice with " + str(number) + " is " + str(result))
print()

number = 5
result = number ** 4
print("Direct computation of twice square is " + str(number) + " is " + str(result))
print()

square = lambda x: x*x

number = 5
result = call_twice(square, number)

print()
print("Calling the square twice with " + str(number) + " is " + str(result))
print()
