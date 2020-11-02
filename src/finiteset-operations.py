from sympy import FiniteSet

set_one = FiniteSet(1, 2, 3)
set_two = FiniteSet(1, 2, 3, 4)

union = set_one.union(set_two)
print("Union:")
print(union)

print()

intersection = set_one.intersection(set_two)
print("Intersection:")
print(intersection)

print()
