even_squares = (x * x for x in range(10)
                    if x % 2 == 0)

print(even_squares)

print("First iteration")
for value in even_squares:
    print(value)

print()

print("Second iteration")
for value in even_squares:
    print(value)
