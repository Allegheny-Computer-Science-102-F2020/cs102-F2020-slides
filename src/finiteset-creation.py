from sympy import FiniteSet

# create a finite set
finite_set = FiniteSet(2, 4, 6, 8, 10)
print("Explicit FiniteSet:")
print(finite_set)
print()

# create an empty set
empty_set = FiniteSet()
print("Empty FiniteSet:")
print(empty_set)
print()

# create a set from a list
list = [2, 4, 6, 8, 10]
finite_set = FiniteSet(*list)
print("FiniteSet from List:")
print(finite_set)
print()

# create a set from a tuple
tuple = (2, 4, 6, 8, 10)
print("FiniteSet from Tuple:")
finite_set = FiniteSet(*tuple)
print(finite_set)
print()

# create a set containing a tuple
tuple = (2, 4, 6, 8, 10)
print("FiniteSet Containing Tuple:")
finite_set = FiniteSet(tuple)
print(finite_set)
print()
