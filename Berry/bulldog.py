class Dog:
    species = "Canis familiaris" # Class  variable, common to all instances


    def __init__(self,name,breed):
        self.name = name # Instance variable
        self.breed = breed


# Creating instances
dog1 = Dog("Rex", "Labrodar")
dog2 = Dog("Bella","Bulldog")

# Accessing class variable
print(dog1.species) # Output
print(dog2.species)


# Changing the class variable
Dog.species = "Canis lupus familiars"

# All instances reflect the change 
print(dog1.species) # Output: Canis lupus familiaris
print(dog2.species) # Output: Canis lupus familiaris