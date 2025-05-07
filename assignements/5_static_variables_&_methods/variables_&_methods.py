# # 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:

    num = 10 # static variable

    @staticmethod
    def add(a:int,b:int)-> int:
        return a + b

m1 = MathUtils()
print(m1.num)  # 10

print(MathUtils.num)  # 10

print(MathUtils.add(2,3))