# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

def add_greeting(cls):
    def greet(self) -> str:
        return "Hello from Decorator!"
    setattr(cls, 'greet', greet)
    return cls

@add_greeting
class Person1:
    def __init__(self, name: str):
        self.name = name

p = Person1("Muhammad Farooq")
print(p.greet())  # type: ignore[attr-defined]
