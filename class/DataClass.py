from dataclasses import dataclass

@dataclass
class Book:
    title : str
    author : str
    year : int
    price : float

    def __post_init__(self):
        if self.year < 1900:
            raise ValueError(f"Provided year:{self.year}")
        

try:
    book1 = Book("The Great Gatsby", "F.Scott Fitzgerald", 1925, 15.99)
    print(book1)

    book2 = Book("A Tale Of Two Cities", "Charles Dickens", 1845, 9.99)
    print(book2)
except ValueError as e:
    print(e)

    