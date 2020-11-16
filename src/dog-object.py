# define a class to represent a Dog entity
class Dog:

    # define the constructor for the Dog class
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

# create an instance of the Dog class for Bosco
bosco = Dog("Bosco", 6, "Havanese")

# display the address of the Bosco instance
print(bosco)
