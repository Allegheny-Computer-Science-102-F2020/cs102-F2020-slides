# sets can store immutable elements
x = {53, 'pencil', (1, 1, 2, 3, 5), 3.14159}

print("Set defined with a multiple types:")
print(x)

print()

# sets cannot store mutable elements
# NOTE: the second assignment statement
# will cause this program to crash!
list = [53, 'pencil', (1, 1, 2, 3, 5), 3.14159]
x = {list}
