def fibonacci_tuple(n):
    result = ( )
    a = 1
    b = 1
    for i in range(n):
        result += (a,)
        a, b = b, a + b
    return result

print(fibonacci_tuple)

for fibonacci_value in fibonacci_tuple(10):
    print(fibonacci_value, end=" ")

print()
