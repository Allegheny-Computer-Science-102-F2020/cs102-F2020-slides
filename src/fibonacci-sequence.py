def fibonacci_sequence(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

print(fibonacci_sequence)

for fibonacci_value in fibonacci_sequence(10):
    print(fibonacci_value, end=" ")

print()
