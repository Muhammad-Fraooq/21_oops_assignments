# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().

def log_function_call(func):
    def wapper():
        print("Before run print function")
        func()
        print("After run print function")
    return wapper

@log_function_call
def say_hello():
    print("Hello World!")
say_hello()
