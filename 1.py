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