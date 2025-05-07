# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.


class Employee:
    def __init__(self):
        # Public Variable
        self.name = "Muhammad Farooq"

        # Protected Variable (convention: use _ before variable)
        self._salary = 50000

        # Private Variable (starts with double underscore)
        self.__ssn = "123-45-6789"

    def Test(self):
        print("Inside Employee class:")
        print(self.name)        # ✅ Public - accessible
        print(self._salary)     # ✅ Protected - accessible within class
        print(self.__ssn)       # ✅ Private - accessible only inside this class

class Demo(Employee):
    def __init__(self):
        super().__init__()  # Call parent class constructor
    
    def Test_1(self):
        print("\nInside Demo (child class):")
        print(self.name)        # ✅ Public - accessible
        print(self._salary)     # ✅ Protected - accessible (since it's child class)
        # print(self.__ssn)     # ❌ Private - Not accessible outside parent class

# Creating object of Employee
e1 = Employee()
e1.Test()

# Access from outside the class
print("\nAccessing from outside the class:")
print(e1.name)        # ✅ Public - accessible
print(e1._salary)     # ⚠️ Protected - technically accessible, but not recommended
# print(e1.__ssn)     # ❌ Private - will raise error

# Creating object of child class
d1 = Demo()
d1.Test_1()

