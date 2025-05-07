# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self,name:str)->None:
        self.name:str = name

class Teacher(Person):
    def __init__(self, name,subject):
        super().__init__(name)
        self.subject = subject

p1 = Person("Muhammad Farooq")
print(p1.name)
t1 = Teacher("Sir Zia Khan","Agentic AI")
print(t1.name)
print(t1.subject)
