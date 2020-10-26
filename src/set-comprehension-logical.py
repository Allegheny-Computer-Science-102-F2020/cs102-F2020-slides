# create a set comprehension for odd positive numbers
# that are less than 20 or the value of 3
odd_positives_two = {n for n in range(20) if n % 2 == 1 or n == 2}

# iterate through the values
for value in odd_positives_two:
    print(value)

# display the values
print()
print(list(odd_positives_two))

print()

# create a set comprehension for even positive numbers
# that are less than 50 and divisible by 4
even_positives_by_four = {n for n in range(20) if n % 2 == 0 and n % 4 == 0}

# iterate through the values
for value in even_positives_by_four:
    print(value)

# display the values
print()
print(list(even_positives_by_four))
