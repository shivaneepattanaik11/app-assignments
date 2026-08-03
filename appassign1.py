class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.available = True

class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Name: ")
        book = Book(book_id, title)
        self.books.append(book)
        print("Book Added Successfully")

    def register_patron(self):
        patron_id = input("Enter Patron ID: ")
        name = input("Enter Patron Name: ")
        patron = Patron(patron_id, name)
        self.patrons.append(patron)
        print("Patron Registered Successfully")

    def borrow_book(self):
        book_id = input("Enter Book ID: ")

        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print("Book Borrowed Successfully")
                else:
                    print("Book is already borrowed")
                return

        print("Book not found")

    def return_book(self):
        book_id = input("Enter Book ID: ")

        for book in self.books:
            if book.book_id == book_id:
                book.available = True
                print("Book Returned Successfully")
                return

        print("Book not found")

    def display_books(self):
        print("\nBooks in Library")
        for book in self.books:
            print("Book ID:", book.book_id)
            print("Book Name:", book.title)
            print("Available:", book.available)
            print()

library = Library()
while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = input("Enter Choice: ")
    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.register_patron()
    elif choice == "3":
        library.borrow_book()
    elif choice == "4":
        library.return_book()
    elif choice == "5":
        library.display_books()
    elif choice == "6":
        print("Thank You")
        break
    else:
        print("Invalid Choice")