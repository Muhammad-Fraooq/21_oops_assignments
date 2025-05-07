# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee1:
    def __init__(self,name):
        self.name = name
    
    def work(self):
        print(f'Employee {self.name} is workig.')

class Department:
    def __init__(self,department):
        self.department = department

    def start_work(self):
        print(f'Department is managing work.')
        self.department.work()

emp = Employee1("Muhammad Farooq")

dept = Department(emp)
dept.start_work()

del emp

dept.start_work()
