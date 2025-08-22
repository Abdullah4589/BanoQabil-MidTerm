library={
    "Harry Potter":("J.K Rowling",True),
    "The Hobbit":("J.R.R. Tolkien",True),
    "1984":("George Orwell",False)
}
transactions = []

def view_books():
    print("\n Available Books")
    for title,(author,available)in library.items():
        if available==True:
            print("Available")
        else:
            print("Not Available")
        print(f"{title} by {author} is {available}.")

def borrow_book():
    try:
        book=input("Enter book you want to borrow:")
        if book not in library:
            raise KeyError("Book not available in library!")
        author,available=library[book]
        if available:
            library[book]=(author,False)
            print(f"You have borrowed '{book}'. ")
            transactions.append({"book": book, "action": "issued"})
        else:
            print(f"Sorry!, '{book}' is not available for borrowing.")

    except KeyError as e:
        print(f"Error! {e}")

def return_book():
    book = input("Enter the book you want to return: ")
    if book in library:
        author, available = library[book]
        if not available:
            library[book] = (author, True)
            print(f"Thank you for returning '{book}'.")
            transactions.append({"book": book, "action": "returned"})
        else:
            print(f"'{book}' was not issued.")
    else:
        print("This book does not belong to our library.")

def add_book():
    title = input("Enter the title of the new book: ")
    author = input("Enter the author of the new book: ")
    if title in library:
        print("Book already exists in the library.")
    else:
        library[title] = (author, True)
        print(f"Book '{title}' by {author} added to the library.")

def search_book():
    search = input("Enter the book title to search: ")
    found = False
    for title, (author, available) in library.items():
        if search.lower() in title.lower():
            print(f"Found: {title} by {author} - {'Available' if available else 'Not Available'}")
            found = True
    if not found:
        print("No matching book found.")

def view_transactions():
    print("\nTransaction History:")
    for t in transactions:
        print(f"Book: {t['book']} - Action: {t['action']}")


def main():
    while True:
        print("\n--- Library Menu ---")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Add Book")
        print("5. Search Book")
        print("6. View Transactions")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            view_books()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            add_book()
        elif choice == '5':
            search_book()
        elif choice == '6':
            view_transactions()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Try again.")

