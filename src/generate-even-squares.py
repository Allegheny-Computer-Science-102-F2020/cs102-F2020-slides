even_squares = (x * x for x in range(10)
                    if x % 2 == 0)

print(even_squares)

for value in even_squares:
    print(value)
