# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self , price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,new_price):
        self.__price = new_price

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self.__price

product1 = Product(200)

print(product1.price)

product1.price = 5000
print(product1.price)

del product1.price