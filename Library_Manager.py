class Library:
    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.record = {}
        self.book_on_lend = []

    def display_books(self):
        for items in self.list_of_books:
            print(items)
        return "This are the books available"

    def add_book(self, name_of_book):
        self.list_of_books.append(name_of_book.upper())
        return self.list_of_books

    def lend_book(self, user, book_required):

        if book_required.upper() in self.list_of_books:

            self.book_on_lend.append(book_required.upper())
            self.list_of_books.remove(book_required.upper())
            self.record[book_required.upper()] = user
            return f"The {book_required} is lended to {user}"

        else:
            return f"Sorry. The {book_required} is currently owned by {self.record[book_required]}"

    def return_book(self, book_to_return):

        self.list_of_books.append(book_to_return.upper())
        self.record.pop(book_to_return.upper())
        return f"{book_to_return} has been returned"

    def display_record(self):
        return self.record


lab_1 = Library(['MY INDIA', 'NIGHT TRAIN AT DEOLI', 'THE UMBRELLA', 'HARRY POTTER', 'GHOST STORIES'],
                'Swati\'s Library')

i = 1

print("Welcome to Student\'s Library.")
while i == 1:
    visitor = input("Enter you name :")
    choice = int(input(
        "You would like to\n1.See available books\n2.Add a book\n3.Lend a book\n4.Return a book\n5.See Record\n6.Exit\nEnter the choice:"))
    if choice == 1:
        print(lab_1.display_books())
        print("-------------------------------------------------------")
    elif choice == 2:
        book_to_add = input("Enter a book to add :")
        print(lab_1.add_book(book_to_add))
        print("-------------------------------------------------------")
    elif choice == 3:
        book_to_lend = input("Enter the book you want :")
        print(lab_1.lend_book(visitor, book_to_lend))
        print("-------------------------------------------------------")
    elif choice == 4:
        book_to_return = input("Enter book to return :")
        print(lab_1.return_book(book_to_return))
        print("-------------------------------------------------------")
    elif choice == 5:
        print(lab_1.display_record())
        print("-------------------------------------------------------")
    else:
        print("-------------------------------------------------------")
        break
