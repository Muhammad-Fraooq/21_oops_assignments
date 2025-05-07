# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

class InvalidAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"Invalid age entered: {age}")

def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    return age

try:
    a = check_age(15)
    print(f"Welcome, your age is : {a}")
except InvalidAgeError as error:
    print(error)
