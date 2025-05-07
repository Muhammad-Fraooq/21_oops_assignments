# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.


class Engine:
    def start(self)->None:
        print("Engine Started!")

class Car1:
    def __init__(self)->None:
        self.engine = Engine() # Create Engine class instance in Car1 class (composition)

    def drive(self)->None:
        self.engine.start()
        print("Car is going!")

my_car = Car1()
my_car.drive()

del my_car # ager Car1 class ko delete kar dya to to Engine class bhi nahi chal gi 

