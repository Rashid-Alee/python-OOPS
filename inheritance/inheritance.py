# inheritance/inheritance.py


# Define the Animal base class
class Animal:
    def __init__(self, name, species):
        self.name = name  # Name of the animal
        self.species = species  # Species of the animal

    def make_sound(self):
        # Placeholder method to be overridden by subclasses
        pass


# Define the Dog subclass that inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(
            name, species="Dog"
        )  # Call the superclass (Animal) constructor
        self.breed = breed  # Breed of the dog

    def make_sound(self):
        # Override the make_sound method to provide a specific implementation
        return "Woof!"


# Example usage of the classes
if __name__ == "__main__":
    # Create an instance of Dog
    my_dog = Dog("Buddy", "Golden Retriever")

    # Print details about the dog
    print(f"{my_dog.name} is a {my_dog.breed} and makes a sound: {my_dog.make_sound()}")
