from sympy import FiniteSet

list = [1, 2, 3, 2]
finite_set = FiniteSet(*list)
print(finite_set)
print()

for element in finite_set:
    print(element)
