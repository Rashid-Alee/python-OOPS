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
        # Initialize the base class (Animal) attributes
        super().__init__(name, species="Dog")
        self.breed = breed  # Breed of the dog

    def make_sound(self):
        # Provide a specific implementation for the Dog class
        return "Woof!"


# Example usage of the classes
if __name__ == "__main__":
    # Create an instance of Dog
    my_dog = Dog("Buddy", "Golden Retriever")

    # Print details about the dog
    print(f"{my_dog.name} is a {my_dog.breed} and makes a sound: {my_dog.make_sound()}")
