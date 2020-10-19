def fibonacci_list(n):
    result = [  ]
    a = 1
    b = 1
    for i in range(n):
        result += (a,)
        a, b = b, a + b
    return result

print(fibonacci_list)

for fibonacci_value in fibonacci_list(10):
    print(fibonacci_value, end=" ")

print()
