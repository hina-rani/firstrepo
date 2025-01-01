class Dog:
  def __init__(self,name,breed):
    self.name = name
    self.breed = breed
  def __str__(self):
    return f"{self.name} is a {self.breed}"

  def __repr__(self):
    return f"Dog('{self.name}','{self.breed}')"

# Creating an instance
dog = Dog("Rex", "Labrador")


# Using print, which calls__str__
print(dog) # Output: Rex is Labrodar


# Using repr, which is often used for debugging
print(repr(dog)) # Output: Dog('Rex is a  Labrodar')

