# define a class to represent a Dog entity
class Dog:

    # define the constructor for the Dog class
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

# create an instance of the Dog class for Bosco
bosco = Dog("Bosco", 6, "Havanese")

# create an instance of the Dog class for Faith
faith = Dog("Faith", 14, "Havanese")

# display the address of the Bosco instance
print(bosco)

print()

print(f"The dog's name is: {bosco.name}")
print(f"The dog's age is: {bosco.age}")
print(f"The dog's breed is: {bosco.breed}")

print()

# display the address of the Faith instance
print(faith)

print()

print(f"The dog's name is: {faith.name}")
print(f"The dog's age is: {faith.age}")
print(f"The dog's breed is: {faith.breed}")

print()
