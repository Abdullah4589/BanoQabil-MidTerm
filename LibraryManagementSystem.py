library = {
    "Harry Potter": ("J.K Rowling", True),
    "The Hobbit": ("J.R.R. Tolkien", True),
    "1984": ("George Orwell", False)
}
transactions = []

def view_books():
    print("\nLibrary Books:")
    for title, (author, available) in library.items():
        status = "available" if available else "not available"
        print(f"{title} by {author} is {status}.")

def borrow_book():
    try:
        user_input = input("Enter book you want to borrow: ")
        
        
        book_found = None
        for title in library.keys():
            if user_input.lower() in title.lower() or title.lower() in user_input.lower():
                book_found = title
                break
        
        if book_found is None:
            raise KeyError("Book not available in library!")
            
        author, available = library[book_found]
        if available:
            library[book_found] = (author, False)
            print(f"You have borrowed '{book_found}'.")
            transactions.append({"book": book_found, "action": "issued"})
        else:
            print(f"Sorry!, '{book_found}' is not available for borrowing.")
    except KeyError as e:
        print(f"Error! {e}")

def return_book():
    user_input = input("Enter the book you want to return: ")
    
    
    book_found = None
    for title in library.keys():
        if user_input.lower() in title.lower() or title.lower() in user_input.lower():
            book_found = title
            break
    
    if book_found:
        author, available = library[book_found]
        if not available:
            library[book_found] = (author, True)
            print(f"Thank you for returning '{book_found}'.")
            transactions.append({"book": book_found, "action": "returned"})
        else:
            print(f"'{book_found}' was not issued.")
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
            status = "Available" if available else "Not Available"
            print(f"Found: {title} by {author} - {status}")
            found = True
    if not found:
        print("No matching book found.")

def view_transactions():
    print("\nTransaction History:")
    if not transactions:
        print("No transactions yet.")
    else:
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
            print("Thank you for using the library system!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()