# Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class

class Car:
    def __init__(self,brand:str)-> None:
        self.brand = brand # public variable

    def start(self)-> None:
        print(f"{self.brand} is starting...")

# create an object of the Car class
car1 = Car("Toyota")

# Accessing the public variable and method
print(f'Car Brand : {car1.brand}')  

# Accessing the public method
car1.start() 
