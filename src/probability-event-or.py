from sympy import FiniteSet

six_sided = FiniteSet(1, 2, 3, 4, 5, 6)
roll_one = FiniteSet(2, 3, 5)
roll_two = FiniteSet(1, 3, 5)

event = roll_one.union(roll_two)
prob = len(event) / len(six_sided)
print(prob)
