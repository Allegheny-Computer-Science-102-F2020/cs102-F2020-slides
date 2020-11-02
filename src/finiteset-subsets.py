from sympy import FiniteSet

set_one = FiniteSet(1, 2, 3)
set_two = FiniteSet(1, 2, 3)

subset = set_one.is_proper_subset(set_two)
print("Set one proper subset set two:")
print(subset)

print()

subset = set_two.is_proper_subset(set_one)
print("Set two proper subset set one:")
print(subset)

print()

set_three = FiniteSet(1, 2, 3, 4)

subset = set_one.is_proper_subset(set_three)
print("Set one proper subset set three:")
print(subset)

print()

subset = set_three.is_proper_subset(set_one)
print("Set three proper subset set one:")
print(subset)
