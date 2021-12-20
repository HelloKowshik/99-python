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
        # self.price = int(self.price - self.price * self.discount)            
        self.price = int(self.price - self.price * StoryBook.discount)            

book1 = StoryBook('Hemlet', 350, 'Shakespeare', 1564, 500)
book2 = StoryBook('A brief history of time', 750, 'Stiphen Hawkings', 1964, 600)
# book1.get_book_info()
# book1.get_author_info()        
# print(book1.no_of_books)
# print(book2.no_of_books)
# print(StoryBook.no_of_books)
print(book1.price)
StoryBook.discount = 0.2
book1.apply_discount()
print(book1.price)
book2.apply_discount()
print(book2.price)
