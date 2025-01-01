class Car:
    def __init__(self, brand, model, year):
        self.brand= brand # Initialize attributes
        self.model= model
        self.year= year
    
    def start(self):
        print(f"{self.brand} {self.model} {self.year} is starting!")

    def stop(self):
        print(f"{self.brand} {self.model} {self.year} is stopping!")

# Create an object
my_car = Car("Toyota", "Corolla", "2022")
my_car.start()
my_car.stop()