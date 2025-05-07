# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    
    def __init__(self, name: str, breed) -> None:
        self.name = name # Instance Variable
        self.breed = breed # Instance Variable 
        
    def bark(self): # Instance Method
        print(f'{self.name} is barking')

dog = Dog("Buddy", "Golden Retriever")
dog.bark()
