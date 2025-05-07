# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC,abstractmethod

class Shape(ABC): # Abstract Class
    @abstractmethod # Abstract Method
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width:float,length:float):
        super().__init__()
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.width

r1 = Rectangle(4,6)
print(f"Rectangle Area: {r1.area()}")  # Output: Rectangle Area: 24

