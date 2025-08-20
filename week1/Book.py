class Book:
    library_name = "My Awesome Library"

    def __init__(self, title, author, isbn, is_checked_out):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

    def display_book_info(self):
        if self.is_checked_out:
            status = "Not Available"
        else:
            status = "available"
        print(f"Book {self.title} of author {self.author} with isbn number {self.isbn} is {status}")

    def check_out(self):
        if self.is_checked_out:
            print(f"Book {self.title} is not available")
        else:
            self.is_checked_out = True
            print(f"Book {self.title} is checked out")
    
    def return_book(self):
        if not self.is_checked_out:
            print(f"Book {self.title} is available already")
        else :
            self.is_checked_out = False
            print(f"Book {self.title} Collected")

book1 = Book("Be Happy", "Om", 1272, False)
book2 = Book("You Are good", "Dadu", 9876, False)
book3 = Book("Do Hard work", "Robert", 8746, False)

book1.display_book_info()
book1.check_out()
book1.display_book_info()
book1.check_out()


book2.display_book_info()
book2.check_out()
book2.return_book()
book2.display_book_info()
book2.return_book()

