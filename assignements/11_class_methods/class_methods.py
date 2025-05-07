# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_book:int = 0

    def __init__(self,book_name:str, author_name:str, price:str):
        self.book_name = book_name
        self.author_name = author_name
        self.price = price 
        Book.total_book += 1 

    @classmethod
    def total_books(cls):
        return cls.total_book
    
    def book_info(self):
        print(f'Book Name : {self.book_name}\nAuthor Name : {self.author_name}\nPrice : {self.price}')

book1 = Book("The Alchemist","Paulo Coelho","$19.99")
book1.book_info()
print(f'Total number of books : {Book.total_books()}')
