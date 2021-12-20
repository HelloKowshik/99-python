class StoryBook:

    no_of_books = 0  # class variable 
    discount = 0.5

    def __init__(self, name, price, author_name, author_born, no_of_pages):
        self.name = name
        self.price = price
        self.author_name = author_name
        self.author_born = author_born
        self.no_of_pages = no_of_pages
        self.published_year = 2020
        StoryBook.no_of_books += 1

    def get_book_info(self):
        print(f'The {self.name} book has {self.no_of_pages} Pages.')

    def get_author_info(self):
        print(f'The book written by {self.author_name} who was born at {self.author_born}.')

    def apply_discount(self):
        self.price = int(self.price - self.price * self.discount)       

    def set_price(self, new_price):
        self.price = new_price                

    #class Method
    @classmethod
    def set_discount(cls, new_discount):
        cls.discount = new_discount

    #class Method
    @classmethod
    def construct_book_from_string(cls, book_str):
        name, price, author_name, author_born, pages = book_str.split(',')
        return cls(name, price, author_name, author_born, pages)

    @staticmethod
    def is_big_book(page):
        if page > 400:
            print('More Then 400 Pages')
        else:
            print('Not More Then 200 Pages')       

book1 = StoryBook('Hemlet', 350, 'Shakespeare', 1564, 500)
book2 = StoryBook('A brief history of time', 750, 'Stiphen Hawkings', 1964, 600)
book_str = 'Harry Porter, 200, JK Rouling, 1970, 480'
book3 = StoryBook.construct_book_from_string(book_str)
# name, price, author_name, author_born, pages = book_str.split(',')
# book3 = StoryBook(name, price, author_name, author_born, pages)
print(book1.price)
print(book3.name)
book1.set_discount(0.6)
book1.apply_discount()
print('After')
print(book1.price)
print(book2.discount)
StoryBook.is_big_book(book2.no_of_pages)
