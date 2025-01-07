class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def apply_discount(self, discount):
        self.price -= self.price * (discount / 100)

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")

# Example 
book = Book("lord of the rings", " J. R. R. Tolkien", 200.00)
book.display_details()
book.apply_discount(100)
book.display_details()