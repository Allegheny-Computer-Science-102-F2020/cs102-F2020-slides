# Reference:
# https://realpython.com/python-sets/

# define the sets
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}

# union
print("Union of the sets:")
print(a.union(b, c, d))
print(a | b | c | d)

print()

# intersection
print("Intersection of the sets:")
print(a.intersection(b, c, d))
print(a & b & c & d)

print()

# difference
print("Difference of the sets:")
print(a.difference(b, c))
print(a - b - c)
