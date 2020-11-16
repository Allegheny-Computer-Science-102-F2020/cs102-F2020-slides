# define a class to represent a Dog entity
class Dog:

    # define the constructor for the Dog class
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # define a description method for the dog
    def description(self):
        return f"{self.name} is a {self.age} years old {self.breed}"

    # define an action method for the dog
    def action(self, action):
        return f"Hey, {self.name} {action}!"

    # define a __str__ method for the dog
    def __str__(self):
        return f"{self.name} is a {self.age} years old {self.breed}"


# create an instance of the Dog class for Bosco
bosco = Dog("Bosco", 6, "Havanese")

# create an instance of the Dog class for Faith
faith = Dog("Faith", 14, "Havanese")

# display the address of the Bosco instance
# note that this only works if __str__ is
# commented out as this controls textual display
# otherwise
print(bosco)

print()

print(f"The dog's name is: {bosco.name}")
print(f"The dog's age is: {bosco.age}")
print(f"The dog's breed is: {bosco.breed}")

print()

# use the description method for Bosco
print(bosco.description())

print()

# use the action method for Bosco
print(bosco.action("roll over"))

print()

# display the address of the Faith instance
# note that this only works if __str__ is
# commented out as this controls textual display
# otherwise
print(faith)

print()

print(f"The dog's name is: {faith.name}")
print(f"The dog's age is: {faith.age}")
print(f"The dog's breed is: {faith.breed}")

print()

# use the description method for Faith
print(faith.description())

print()

# use the action method for Bosco
print(faith.action("waive bye-bye"))

print()
