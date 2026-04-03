class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def display(self):
        status = "Available" if self.is_available else "Issued"
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}")


# Class for Member
class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)


# Class for Library
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    # Add book
    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    # Add member
    def add_member(self, member):
        self.members.append(member)
        print("Member added successfully!")

    # Display all books
    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                book.display()

    # Find book by ID
    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    # Find member by ID
    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    # Issue book
    def lend_book(self, book_id, member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)

        if book and member:
            if book.is_available:
                book.is_available = False
                member.borrow_book(book)
                print("Book issued successfully!")
            else:
                print("Book is already issued.")
        else:
            print("Book or Member not found.")

    # Return book
    def return_book(self, book_id, member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)

        if book and member:
            if book in member.borrowed_books:
                book.is_available = True
                member.return_book(book)
                print("Book returned successfully!")
            else:
                print("This member did not borrow this book.")
        else:
            print("Book or Member not found.")


# Main Program (Menu-driven)
library = Library()

while True:
    print("\n===== Library Menu =====")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Display Books")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        library.add_book(Book(book_id, title, author))

    elif choice == "2":
        member_id = int(input("Enter Member ID: "))
        name = input("Enter Name: ")
        library.add_member(Member(member_id, name))

    elif choice == "3":
        library.display_books()

    elif choice == "4":
        book_id = int(input("Enter Book ID: "))
        member_id = int(input("Enter Member ID: "))
        library.lend_book(book_id, member_id)

    elif choice == "5":
        book_id = int(input("Enter Book ID: "))
        member_id = int(input("Enter Member ID: "))
        library.return_book(book_id, member_id)

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")