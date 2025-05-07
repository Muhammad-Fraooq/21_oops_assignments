# # 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.


class Counter:
    count = 0  # class variable

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total objects created: {cls.count}")

c1 = Counter()
print(c1.count)  # 1
c2 = Counter()  
print(c2.count)  # 2
c3 = Counter()
print(c3.count)  # 3
Counter.show_count()  # Total objects created: 3
