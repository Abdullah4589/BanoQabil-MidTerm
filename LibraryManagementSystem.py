import tkinter as tk
from tkinter import messagebox, simpledialog

# Initialize library and transactions
library = {
    "Harry Potter": ("J.K Rowling", True),
    "The Hobbit": ("J.R.R. Tolkien", True),
    "1984": ("George Orwell", False)
}

transactions = []

# Functions
def view_books():
    books_window = tk.Toplevel(root)
    books_window.title("Library Books")
    tk.Label(books_window, text="Library Books", font=("Arial", 14, "bold")).pack(pady=10)
    
    for title, (author, available) in library.items():
        status = "Available" if available else "Not Available"
        tk.Label(books_window, text=f"{title} by {author} - {status}").pack(anchor="w")

def borrow_book():
    book = simpledialog.askstring("Borrow Book", "Enter book title to borrow:")
    if book:
        book_found = None
        for title in library.keys():
            if book.lower() in title.lower():
                book_found = title
                break
        if book_found:
            author, available = library[book_found]
            if available:
                library[book_found] = (author, False)
                transactions.append({"book": book_found, "action": "issued"})
                messagebox.showinfo("Success", f"You borrowed '{book_found}'.")
            else:
                messagebox.showwarning("Unavailable", f"'{book_found}' is not available.")
        else:
            messagebox.showerror("Error", "Book not found in the library.")

def return_book():
    book = simpledialog.askstring("Return Book", "Enter book title to return:")
    if book:
        book_found = None
        for title in library.keys():
            if book.lower() in title.lower():
                book_found = title
                break
        if book_found:
            author, available = library[book_found]
            if not available:
                library[book_found] = (author, True)
                transactions.append({"book": book_found, "action": "returned"})
                messagebox.showinfo("Success", f"Thank you for returning '{book_found}'.")
            else:
                messagebox.showinfo("Info", f"'{book_found}' was not issued.")
        else:
            messagebox.showerror("Error", "This book does not belong to the library.")

def add_book():
    title = simpledialog.askstring("Add Book", "Enter book title:")
    author = simpledialog.askstring("Add Book", "Enter author name:")
    if title and author:
        if title in library:
            messagebox.showinfo("Exists", "Book already exists in the library.")
        else:
            library[title] = (author, True)
            messagebox.showinfo("Success", f"Book '{title}' by {author} added.")

def search_book():
    search = simpledialog.askstring("Search Book", "Enter title to search:")
    if search:
        result_window = tk.Toplevel(root)
        result_window.title("Search Results")
        tk.Label(result_window, text="Search Results", font=("Arial", 14, "bold")).pack(pady=10)
        
        found = False
        for title, (author, available) in library.items():
            if search.lower() in title.lower():
                status = "Available" if available else "Not Available"
                tk.Label(result_window, text=f"{title} by {author} - {status}").pack(anchor="w")
                found = True
        if not found:
            tk.Label(result_window, text="No matching book found.").pack()

def view_transactions():
    trans_window = tk.Toplevel(root)
    trans_window.title("Transactions")
    tk.Label(trans_window, text="Transaction History", font=("Arial", 14, "bold")).pack(pady=10)
    
    if not transactions:
        tk.Label(trans_window, text="No transactions yet.").pack()
    else:
        for t in transactions:
            tk.Label(trans_window, text=f"Book: {t['book']} - Action: {t['action']}").pack(anchor="w")

# Main GUI Window
root = tk.Tk()
root.title("Library Management System")
root.geometry("400x400")
root.config(bg="#f0f0f0")

# Title
tk.Label(root, text="Library Management System", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=20)

# Buttons
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="View Books", width=20, command=view_books).grid(row=0, column=0, pady=5)
tk.Button(btn_frame, text="Borrow Book", width=20, command=borrow_book).grid(row=1, column=0, pady=5)
tk.Button(btn_frame, text="Return Book", width=20, command=return_book).grid(row=2, column=0, pady=5)
tk.Button(btn_frame, text="Add Book", width=20, command=add_book).grid(row=3, column=0, pady=5)
tk.Button(btn_frame, text="Search Book", width=20, command=search_book).grid(row=4, column=0, pady=5)
tk.Button(btn_frame, text="View Transactions", width=20, command=view_transactions).grid(row=5, column=0, pady=5)
tk.Button(btn_frame, text="Exit", width=20, command=root.quit).grid(row=6, column=0, pady=5)

root.mainloop()
