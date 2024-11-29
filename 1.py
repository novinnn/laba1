from datetime import datetime
import json
import xml.etree.ElementTree as ET
from typing import List, Optional

# Класс книги
class Book:
    def __init__(self, title: str, author: 'Author', price: float, genre: 'Genre', publication_date: datetime):
        self.title = title  
        self.author = author  
        self.price = float(price)  
        self.genre = genre 
        self.publication_date = publication_date  
        self.is_available = True  

    # Метод для применения скидки на книгу
    def discount(self, percentage: float) -> None:
        self.price *= (1 - float(percentage) / 100)  

# Класс автора
class Author:
    def __init__(self, name: str, bio: str):
        self.name = name  
        self.bio = bio  
        self.books: List[Book] = [] 

    
    def add_book(self, book: 'Book') -> None:
        self.books.append(book)

# Класс покупателя
class Customer:
    def __init__(self, name: str, email: str, balance: float):
        self.name = name  
        self.email = email  
        self.balance = float(balance) 
        self.purchases: List[Book] = []  

    # Метод для покупки книги
    def buy_book(self, book: 'Book') -> None:
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

# Класс заказа
class Order:
    def __init__(self, customer: 'Customer', book: 'Book', date: Optional[datetime] = None):
        self.customer = customer  
        self.book = book  
        self.date = date or datetime.now()  
        self.is_completed = False 

    
    def complete_order(self) -> None:
        self.is_completed = True  

# Класс отзыва
class Review:
    def __init__(self, customer: 'Customer', book: 'Book', rating: int, comment: str):
        self.customer = customer  
        self.book = book  
        self.rating = int(rating)  
        self.comment = comment 
        self.date = datetime.now() 

# Класс жанра
class Genre:
    def __init__(self, name: str):
        self.name = name  
        self.books: List[Book] = []  

   
    def add_book(self, book: 'Book') -> None:
        self.books.append(book)

# Класс издателя
class Publisher:
    def __init__(self, name: str):
        self.name = name  
        self.books_published: List[Book] = [] 

    
    def publish_book(self, book: 'Book') -> None:
        self.books_published.append(book)

# Класс корзины покупателя
class Cart:
    def __init__(self, customer: 'Customer'):
        self.customer = customer 
        self.items: List[Book] = []  

    
    def add_to_cart(self, book: 'Book') -> None:
        self.items.append(book)

    
    def remove_from_cart(self, book: 'Book') -> None:
        self.items.remove(book)

# Класс скидочного кода
class DiscountCode:
    def __init__(self, code: str, percentage: float, expiry_date: datetime):
        self.code = code 
        self.percentage = float(percentage)  
        self.expiry_date = expiry_date 
        self.is_used = False  

    # Метод для применения скидки к книге
    def apply_discount(self, book: 'Book') -> None:
        if not self.is_used and datetime.now() <= self.expiry_date: 
            book.discount(self.percentage) 
            self.is_used = True  

# Класс цифровой библиотеки
class DigitalLibrary:
    def __init__(self):
        self.books: List[Book] = []  

    # Метод для добавления книги в библиотеку
    def add_book(self, book: 'Book') -> None:
        self.books.append(book)

    # Метод для поиска книг по ключевому слову
    def search_books(self, keyword: str) -> List['Book']:
        return [book for book in self.books if keyword.lower() in book.title.lower()]

# Функция для сохранения библиотеки в формате JSON
def save_to_json(digital_library: 'DigitalLibrary', filename: str = "library.json") -> None:
    books_data: List[dict] = []  
    for book in digital_library.books:
        books_data.append({
            "title": str(book.title), 
            "author": str(book.author.name),  
            "price": float(book.price), 
            "genre": str(book.genre.name), 
            "publication_date": str(book.publication_date.isoformat()) 
        })
    with open(filename, 'w') as f:
        json.dump(books_data, f, indent=4) 

# Функция для загрузки библиотеки из формата JSON
def load_from_json(filename: str = "library.json") -> List['Book']:
    with open(filename, 'r') as f:
        books_data: List[dict] = json.load(f)  
        books: List[Book] = []  
        for book_data in books_data:
            author = Author(str(book_data["author"]), "")  
            genre = Genre(str(book_data["genre"]))  
            book = Book(
                title=str(book_data["title"]),
                author=author,
                price=float(book_data["price"]),
                genre=genre,
                publication_date=datetime.fromisoformat(str(book_data["publication_date"]))
            )
            books.append(book)  
        return books

# Функция для сохранения библиотеки в формате XML
def save_to_xml(digital_library: 'DigitalLibrary', filename: str = "library.xml") -> None:
    library = ET.Element("library") 
    for book in digital_library.books:
        book_elem = ET.SubElement(library, "book")  
        ET.SubElement(book_elem, "title").text = str(book.title)  
        ET.SubElement(book_elem, "author").text = str(book.author.name)  
        ET.SubElement(book_elem, "price").text = str(float(book.price))  
        ET.SubElement(book_elem, "genre").text = str(book.genre.name)  
        ET.SubElement(book_elem, "publication_date").text = str(book.publication_date.isoformat()) 
    
    tree = ET.ElementTree(library)  
    tree.write(filename)  

# Функция для загрузки библиотеки из формата XML
def load_from_xml(filename: str = "library.xml") -> List['Book']:
    tree = ET.parse(filename) 
    root = tree.getroot()  
    books: List[Book] = [] 
    for book_elem in root.findall("book"):  

        title = str(book_elem.find("title").text)  
        author_name = str(book_elem.find("author").text)  
        price = float(book_elem.find("price").text)  
        genre_name = str(book_elem.find("genre").text)  
        publication_date = datetime.fromisoformat(str(book_elem.find("publication_date").text))  
        
        author = Author(author_name, "")  
        genre = Genre(genre_name)  
        book = Book(title, author, price, genre, publication_date)  
        books.append(book)  
    return books
