<<<<<<< HEAD
# Library Management System (Console Version)

# Initialize library and transactions
# library dictionary format: "Book Title": ("Author Name", Availability Status)
=======
# Initialize a dictionary to store library books.
# Format: "Book Title": ("Author Name", Availability Status)
>>>>>>> parent of 380d18d (Update LibraryManagementSystem.py)
# Availability: True = Available, False = Not Available
library = {
    "Harry Potter": ("J.K Rowling", True),
    "The Hobbit": ("J.R.R. Tolkien", True),
    "1984": ("George Orwell", False),
    "Jannat ke Pattay": ("Nimrah Ahmed", True),
    "The Alchemist": ("Paulo Coelho", False),
    "To Kill a Mockingbird": ("Harper Lee", True)
}

<<<<<<< HEAD
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
=======
# List to keep track of all borrow and return transactions
transactions = []

# Function to display all books in the library with their status
def view_books():
    print("\nLibrary Books:")
    # Loop through each book in the library dictionary
    for title, (author, available) in library.items():
        status = "available" if available else "not available"
        print(f"{title} by {author} is {status}.")

# Function to borrow a book from the library
def borrow_book():
    try:
        # Ask the user to enter the book title they want to borrow
        user_input = input("Enter book you want to borrow: ")
        
        # Search for the book in the library (case-insensitive match)
        book_found = None
        for title in library.keys():
            if user_input.lower() in title.lower() or title.lower() in user_input.lower():
                book_found = title
                break
        
        # If the book is not in the library, raise an error
        if book_found is None:
            raise KeyError("Book not available in library!")
            
        author, available = library[book_found]
        # If the book is available, mark it as borrowed
        if available:
            library[book_found] = (author, False)
            print(f"You have borrowed '{book_found}'.")
            transactions.append({"book": book_found, "action": "issued"})
        else:
            # If the book is already borrowed
            print(f"Sorry!, '{book_found}' is not available for borrowing.")
    except KeyError as e:
        # Handle the case when the book is not in the library
        print(f"Error! {e}")

# Function to return a borrowed book
def return_book():
    # Ask the user to enter the book title they want to return
    user_input = input("Enter the book you want to return: ")
    
    # Search for the book in the library
    book_found = None
    for title in library.keys():
        if user_input.lower() in title.lower() or title.lower() in user_input.lower():
            book_found = title
            break
    
    if book_found:
        author, available = library[book_found]
        # Check if the book was borrowed
        if not available:
            library[book_found] = (author, True)
            print(f"Thank you for returning '{book_found}'.")
            transactions.append({"book": book_found, "action": "returned"})
        else:
            # If the book was never issued
            print(f"'{book_found}' was not issued.")
    else:
        # Book does not belong to this library
        print("This book does not belong to our library.")

# Function to add a new book to the library
def add_book():
    title = input("Enter the title of the new book: ")
    author = input("Enter the author of the new book: ")
    # Check if the book already exists
    if title in library:
        print("Book already exists in the library.")
    else:
        # Add the new book with availability set to True
        library[title] = (author, True)
        print(f"Book '{title}' by {author} added to the library.")

# Function to search for a book by its title
def search_book():
    search = input("Enter the book title to search: ")
    found = False
    # Loop through all books and search for a match
    for title, (author, available) in library.items():
        if search.lower() in title.lower():
            status = "Available" if available else "Not Available"
            print(f"Found: {title} by {author} - {status}")
>>>>>>> parent of 380d18d (Update LibraryManagementSystem.py)
            found = True
    if not found:
        print("No matching book found.")

<<<<<<< HEAD
# Function to view transaction history
=======
# Function to view all past transactions (borrow and return)
>>>>>>> parent of 380d18d (Update LibraryManagementSystem.py)
def view_transactions():
    print("\nTransaction History:")
    if not transactions:
        print("No transactions yet.")
    else:
        for t in transactions:
            print(f"Book: {t['book']} - Action: {t['action']}")

<<<<<<< HEAD
# Main menu function to interact with the user
def main():
    while True:
        print("\n=== Library Management System ===")
=======
# Main function to display the menu and handle user input
def main():
    while True:
        # Display the library menu options
        print("\n--- Library Menu ---")
>>>>>>> parent of 380d18d (Update LibraryManagementSystem.py)
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Add Book")
        print("5. Search Book")
        print("6. View Transactions")
        print("7. Exit")
<<<<<<< HEAD

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
=======
        
        choice = input("Enter your choice: ")
        
        # Execute the corresponding function based on user input
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

# Run the program
>>>>>>> parent of 380d18d (Update LibraryManagementSystem.py)
if __name__ == "__main__":
    main()
