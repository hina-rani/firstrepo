class Car:
    def __init__(self, brand, model, year):
        self.brand= brand # Initialize attributes
        self.model= model
        self.year= year
    def get(self):
        print(self.brand)
        print(self.model)
        print(self.year)

# Create objects with attrtibutes initialized
car1 = Car("Toyota", "Corolla", "2022")
car2 = Car( "Toyota", "Corolla", "2022")
car3 = Car("Toyota", "Revo", "2016")
car4 = Car("Suzuki", "Alto", "2022") 

car1.get(),car2.get()