def fibonacci_generator(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

print(fibonacci_generator)

for fibonacci_value in fibonacci_generator(10):
    print(fibonacci_value, end=" ")

print()
