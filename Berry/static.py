class Mathutils:
    @staticmethod
    def add(x, y):
        return x + y
         
    @staticmethod
    def multiply(x, y):
     return x * y

# Calling static methods  without creating an instance of the class
print(Mathutils.add(2, 3))  
print(Mathutils.multiply(2, 3))