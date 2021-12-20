class StoryBook:
    no_of_books = 0
    discount = 0.5

    def __init__(self, name, price, author_name, author_born, no_of_pages):
        self.name = name
        self.price = price
        self.author_name = author_name
        self.author_born = author_born
        self.no_of_pages = no_of_pages
        StoryBook.no_of_books += 1

    def get_book_info(self):
        print(f'Book name: {self.name}, Price: {self.price}, Total Page: {self.no_of_pages}')

    def get_author_info(self):
        print(f'Author Name: {self.author_name}, Born in {self.author_born}')

    def apply_discount(self):
        self.price = int(self.price - StoryBook.discount * self.price)


class Library:
    def __init__(self, book_list = None):
        if book_list is None:
            self.book_list = []
        else:
            self.book_list = book_list

    def get_all_books(self):
        for book in self.book_list:
            print(f'Title: {book.name}, Author: {book.author_name}, Price: {book.price}')

    def add_book(self, book):
        self.book_list.append(book)

    def remove_book(self, book):
        self.book_list.remove(book)                        


book_1 = StoryBook('Hamlet', 350, 'Shakespeare', 1564, 500)
book_2 = StoryBook('The Kite Runner', 200, 'Khaled Hossaini', 1965, 200)

lib_1 = Library()
lib_1.add_book(book_1)
lib_1.add_book(book_2)
lib_1.remove_book(book_2)
lib_1.get_all_books()
