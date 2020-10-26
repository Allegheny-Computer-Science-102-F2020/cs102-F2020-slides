# create a set comprehension for odd positive numbers
# that are less than 100
odd_positives = {n for n in range(100) if n % 2 == 1}

# iterate through the odd positives
for odd_positive in odd_positives:
    print(odd_positive)

# display the odd positives
print()
print(list(odd_positives))

# create a set comprehension for even positive numbers
# that are less than 100
even_positives = {n for n in range(100) if n % 2 == 0}

# iterate through the even positives
for even_positive in even_positives:
    print(even_positive)

# display the even positives
print()
print(list(even_positives))
