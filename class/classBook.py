class Book:
    toal_books = 0
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
        Book.toal_books += 1

    def introduce(self):
        print(f"Book: {self.name}, Author: {self.author}, Year: {self.year}.")

    @classmethod
    def show_toal_books(cls):
        print(f"Total number of books: {cls.toal_books}")

    
book1 = Book("Samfonie mordegan", "Abbass Marufi", 2001)
book2 = Book("You can heal your life", "Lueise L.hey", 1987)

book1.introduce()
book2.introduce()
Book.show_toal_books()
