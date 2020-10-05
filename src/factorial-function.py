def factorial(number: int):
    print(f"Current call factorial({number})")
    if number == 1:
        print("  ... Hit the base case!")
        return 1
    print(f"  ... Now calling factorial({number-1})")
    return number * factorial(number - 1)

num = 5
print()
print("The factorial of " + str(num) + " is " + str(factorial(num)))
print()
