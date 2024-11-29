from datetime import datetime
import json
import xml.etree.ElementTree as ET

class Book:
    def __init__(self, title, author, price, genre, publication_date):
        self.title = title
        self.author = author
        self.price = price
        self.genre = genre
        self.publication_date = publication_date
        self.is_available = True

    def discount(self, percentage):
        self.price *= (1 - percentage / 100)

class Author:
    def __init__(self, name, bio):
        self.name = name
        self.bio = bio
        self.books = []

    def add_book(self, book):
        self.books.append(book)

class Customer:
    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = balance
        self.purchases = []

    def buy_book(self, book):
        try:
            if not book.is_available:
                raise ValueError("Book is unavailable.")
            if self.balance < book.price:
                raise ValueError("Not enough balance.")
            self.balance -= book.price
            self.purchases.append(book)
            book.is_available = False
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

class Order:
    def __init__(self, customer, book, date=None):
        self.customer = customer
        self.book = book
        self.date = date or datetime.now()
        self.is_completed = False

    def complete_order(self):
        self.is_completed = True

class Review:
    def __init__(self, customer, book, rating, comment):
        self.customer = customer
        self.book = book
        self.rating = rating
        self.comment = comment
        self.date = datetime.now()

class Genre:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

class Publisher:
    def __init__(self, name):
        self.name = name
        self.books_published = []

    def publish_book(self, book):
        self.books_published.append(book)

class Cart:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_to_cart(self, book):
        self.items.append(book)

    def remove_from_cart(self, book):
        self.items.remove(book)

class DiscountCode:
    def __init__(self, code, percentage, expiry_date):
        self.code = code
        self.percentage = percentage
        self.expiry_date = expiry_date
        self.is_used = False

    def apply_discount(self, book):
        if not self.is_used and datetime.now() <= self.expiry_date:
            book.discount(self.percentage)
            self.is_used = True

class DigitalLibrary:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_books(self, keyword):
        return [book for book in self.books if keyword.lower() in book.title.lower()]
    
#я случайно неправильно иниты написал


