from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    @abstractmethod
    def display(): pass

# MyBook class inherits from Book class
class MyBook(Book):

    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title:", title)
        print("Author:", author)
        print("Price:", price)

title=input("Enter a book title: ")
author=input("Enter the book's author: ")
price=int(input("Enter a price: "))
new_novel=MyBook(title,author,price)
new_novel.display()