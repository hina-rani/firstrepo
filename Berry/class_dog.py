class Dog:
    # Constructor (initializer)
    def __init__(self, name, breed):
        self.name = name # Instance variable
        self.breed = breed # Instance variable

    # Method (behavoir)
    def bark(self):
        print(f"{self.name} says woof!")


    def get_breed(self):
        return self.breed   
    
dog1 = Dog("Rex", "Labrador")
dog2 = Dog("Bella", "Bulldog")

# Accessing attributes
print(dog1.name)
print(dog2.get_breed()) 