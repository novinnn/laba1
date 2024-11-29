from datetime import datetime

class Book:
    def init(self, title, author, price, genre, publication_date):
        self.title = title
        self.author = author
        self.price = price
        self.genre = genre
        self.publication_date = publication_date
        self.is_available = True

    def discount(self, percentage):
        self.price *= (1 - percentage / 100)
        
class Author:
    def init(self, name, bio):
        self.name = name
        self.bio = bio
        self.books = []

    def add_book(self, book):
        self.books.append(book)

class Customer:
    def init(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = balance
        self.purchases = []

    def buy_book(self, book):
        if book.is_available and self.balance >= book.price:
            self.balance -= book.price
            self.purchases.append(book)
            book.is_available = False
        else:
            raise ValueError("Not enough balance or book is unavailable.")