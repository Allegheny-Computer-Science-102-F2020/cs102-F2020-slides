def square(number: int):
    print(f"Called square({number})")
    print(f"  returning {number*number}")
    return number * number


def call_twice(f, number: int):
    print(f"Calling twice {f} with starting number of {number}")
    return f(f(number))


number = 5
result = call_twice(square, number)

print()
print("Calling the square twice with " + str(number) + " is " + str(result))
print()

number = 5
result = number ** 4
print("Direct computation of twice square is " + str(number) + " is " + str(result))
print()

square_lambda = lambda x: x*x

number = 5
result = call_twice(square_lambda, number)

print("Calling the square lambda twice with " + str(number) + " is " + str(result))
print()
