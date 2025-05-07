# # 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self,name:str,marks:int)-> None:
        self.name = name
        self.marks = marks
        
    def display(self)-> None:
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("Muhammad Farooq", 85)
s2 = Student("Muhammad Suleman", 90)
s1.display()
s2.display()
