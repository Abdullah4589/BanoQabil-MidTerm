# Library Management System (Console Version)

# Initialize library and transactions
# library dictionary format: "Book Title": ("Author Name", Availability Status)
# Availability: True = Available, False = Not Available
library = {
    "Harry Potter": ("J.K Rowling", True),
    "The Hobbit": ("J.R.R. Tolkien", True),
    "1984": ("George Orwell", False),
    "Jannat ke Pattay": ("Nimrah Ahmed", True),
    "The Alchemist": ("Paulo Coelho", False),
    "To Kill a Mockingbird": ("Harper Lee", True)
}

# List to store borrow and return transactions
transactions = []

# Function to view all books in the library with their availability status
def view_books():
    print("\nLibrary Books:")
    for title, (author, available) in library.items():
        status = "Available" if available else "Not Available"
        print(f"{title} by {author} - {status}")

# Function to borrow a book from the library
def borrow_book():
    book = input("\nEnter book title to borrow: ").strip()
    book_found = None
    
    # Check if the entered title matches any book in the library
    for title in library.keys():
        if book.lower() in title.lower():
            book_found = title
            break
    
    if book_found:
        author, available = library[book_found]
        # If book is available, mark it as borrowed (False)
        if available:
            library[book_found] = (author, False)
            transactions.append({"book": book_found, "action": "issued"})
            print(f"You borrowed '{book_found}'.")
        else:
            print(f"'{book_found}' is not available.")
    else:
        print("Book not found in the library.")

# Function to return a borrowed book
def return_book():
    book = input("\nEnter book title to return: ").strip()
    book_found = None
    
    # Check if the book exists in the library
    for title in library.keys():
        if book.lower() in title.lower():
            book_found = title
            break
    
    if book_found:
        author, available = library[book_found]
        # If book is currently borrowed, mark it as available again
        if not available:
            library[book_found] = (author, True)
            transactions.append({"book": book_found, "action": "returned"})
            print(f"Thank you for returning '{book_found}'.")
        else:
            print(f"'{book_found}' was not issued.")
    else:
        print("This book does not belong to the library.")

# Function to add a new book to the library
def add_book():
    title = input("\nEnter book title: ").strip()
    author = input("Enter author name: ").strip()
    
    # Check if the title and author are valid
    if title and author:
        if title in library:
            print("Book already exists in the library.")
        else:
            library[title] = (author, True)  # New book is available by default
            print(f"Book '{title}' by {author} added.")
    else:
        print("Invalid input. Both title and author are required.")

# Function to search for a book by title
def search_book():
    search = input("\nEnter title to search: ").strip()
    found = False
    
    # Check all books for a matching title
    for title, (author, available) in library.items():
        if search.lower() in title.lower():
            status = "Available" if available else "Not Available"
            print(f"{title} by {author} - {status}")
            found = True
    if not found:
        print("No matching book found.")

# Function to view transaction history
def view_transactions():
    print("\nTransaction History:")
    if not transactions:
        print("No transactions yet.")
    else:
        for t in transactions:
            print(f"Book: {t['book']} - Action: {t['action']}")

# Main menu function to interact with the user
def main():
    while True:
        print("\n=== Library Management System ===")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Add Book")
        print("5. Search Book")
        print("6. View Transactions")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        # Perform actions based on user's choice
        if choice == "1":
            view_books()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            add_book()
        elif choice == "5":
            search_book()
        elif choice == "6":
            view_transactions()
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()
