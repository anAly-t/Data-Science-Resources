# Exercise: Building a Class for a Bookstore:

# Define a class for a book with attributes like title, author, and price.
# Create a separate class for a bookstore that can manage an inventory of books.
# Add methods for adding new books, displaying the inventory, and calculating the total value of the inventory.
    
class Book:
    def __init__(self, title, author, price):
        """
        Initialize a Book with title, author, and price.
        """
        self.title = title
        self.author = author
        self.price = price

class Bookstore:
    def __init__(self):
        """
        Initialize a Bookstore with an empty inventory.
        """
        self.inventory = []

    def add_book(self, book):
        """
        Add a new book to the bookstore's inventory.
        """
        self.inventory.append(book)
        print(f"Added '{book.title}' by {book.author} to the inventory.")

    def display_inventory(self):
        """
        Display the details of all books in the inventory.
        """
        print("Bookstore Inventory:")
        for book in self.inventory:
            print(f"Title: {book.title}, Author: {book.author}, Price: ${book.price}")

    def calculate_total_value(self):
        """
        Calculate the total value of the inventory by summing up the prices of all books.
        """
        total_value = sum(book.price for book in self.inventory)
        print(f"Total Inventory Value: ${total_value}")

# Creating instances of the Book class
book1 = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", price=15)
book2 = Book(title="To Kill a Mockingbird", author="Harper Lee", price=20)
book3 = Book(title="1984", author="George Orwell", price=18)

# Creating an instance of the Bookstore class
bookstore = Bookstore()

# Adding books to the inventory
bookstore.add_book(book1)
bookstore.add_book(book2)
bookstore.add_book(book3)

# Displaying the inventory
bookstore.display_inventory()

# Calculating the total value of the inventory
bookstore.calculate_total_value()


# In this code:

# - The `Book` class represents a book with attributes like title, author, and price.
# - The `Bookstore` class has methods for adding new books, displaying the inventory, and calculating the total value of the inventory.
# - Instances of the `Book` class are created for sample books.
# - An instance of the `Bookstore` class is created.
# - Books are added to the bookstore's inventory using the `add_book` method.
# - The `display_inventory` method is used to display the details of all books in the inventory.
# - The `calculate_total_value` method is used to calculate the total value of the inventory.