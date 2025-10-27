"""
Problem 3: Book Library
 Create a  Book  class with:
 Attributes:  title ,  author ,  available  (True/False)
 Method:  borrow()  - book ko unavailable kare if available hai
 Method:  return_book()  - book ko available kare
 Method:  book_info()  - book details display kare
 Expected Output:
 Title: The Alchemist
 Author: Paulo Coelho
 Available: Yes
 Book borrowed successfully!
 Available: No
 """

class Book:
    def __init__(self,title,author,available=True):
        self.title = title
        self.author = author
        self.available = available
    
    def borrow(self):
        if self.available == True:
            print("Book borrowed successfully!")
            self.available = False
            print("Available: No")
    
    def return_book(self):
        self.available = True

    def book_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        
my_book = Book("The Alchemist","Paulo Coelho")
my_book.book_info()
my_book.borrow()


