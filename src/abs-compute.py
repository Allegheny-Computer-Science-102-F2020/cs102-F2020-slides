#!/bin/python3

def absone(n):
    if n >= 0:
        return n
    else:
        return -n

def abstwo(n):
    if n >= 0:
        return n
    return -n

print(str(absone(10)))
print(str(absone(-10)))

print()

print(str(abstwo(10)))
print(str(abstwo(-10)))
